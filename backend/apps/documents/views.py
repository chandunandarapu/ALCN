from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Document, DocumentVersion
from .serializers import DocumentSerializer, DocumentVersionSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """Document management and versioning"""
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['project', 'document_type', 'is_public', 'is_final']
    ordering_fields = ['-created_at', 'title']
    
    def get_queryset(self):
        return Document.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
    
    @action(detail=True, methods=['post'])
    def upload_new_version(self, request, pk=None):
        """Upload a new version of the document"""
        document = self.get_object()
        file = request.FILES.get('file')
        change_notes = request.data.get('change_notes', '')
        
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create new version
        new_version = document.version + 1
        DocumentVersion.objects.create(
            document=document,
            version_number=new_version,
            file=file,
            changed_by=request.user,
            change_notes=change_notes
        )
        
        # Update document
        document.version = new_version
        document.file = file
        document.file_size = file.size
        document.save()
        
        return Response({'status': 'version_uploaded', 'new_version': new_version})
    
    @action(detail=True, methods=['get'])
    def versions(self, request, pk=None):
        """Get all versions of a document"""
        document = self.get_object()
        versions = document.versions.all()
        serializer = DocumentVersionSerializer(versions, many=True)
        return Response(serializer.data)
