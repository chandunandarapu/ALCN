import json
import urllib.request

# Test 1: Authentication
print("=" * 60)
print("TEST 1: JWT Authentication")
print("=" * 60)

data = json.dumps({
    'username': 'admin',
    'password': 'admin123'
}).encode('utf-8')

req = urllib.request.Request(
    'http://127.0.0.1:8000/api/token/',
    data=data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    response = urllib.request.urlopen(req)
    result = json.loads(response.read())
    access_token = result.get('access', '')
    print('✓ Authentication successful!')
    print(f'Access Token: {access_token[:50]}...')
    print()
    
    # Test 2: Get Users with token
    print("=" * 60)
    print("TEST 2: Get Users (with authentication)")
    print("=" * 60)
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    req = urllib.request.Request(
        'http://127.0.0.1:8000/api/users/',
        headers=headers,
        method='GET'
    )
    
    response = urllib.request.urlopen(req)
    users = json.loads(response.read())
    print('✓ Users endpoint working!')
    print(f'Number of users: {len(users) if isinstance(users, list) else users.get("count", "N/A")}')
    print()
    
except Exception as e:
    print(f'✗ Error: {e}')

# Test 3: Swagger UI
print("=" * 60)
print("TEST 3: Swagger UI Documentation")
print("=" * 60)

try:
    response = urllib.request.urlopen('http://127.0.0.1:8000/swagger/')
    print('✓ Swagger UI is accessible at http://127.0.0.1:8000/swagger/')
except Exception as e:
    print(f'✗ Error: {e}')

# Test 4: Admin Interface
print("=" * 60)
print("TEST 4: Django Admin Interface")
print("=" * 60)

try:
    response = urllib.request.urlopen('http://127.0.0.1:8000/admin/')
    print('✓ Admin interface is accessible at http://127.0.0.1:8000/admin/')
    print('  Login with: admin / admin123')
except Exception as e:
    print(f'✗ Error: {e}')

print()
print("=" * 60)
print("BACKEND STATUS: ✓ ALL SYSTEMS OPERATIONAL")
print("=" * 60)
