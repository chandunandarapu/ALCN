import { Routes, Route, Navigate } from "react-router-dom";

import Login from "../pages/auth/Login";

import AdminDashboard from "../pages/admin/Dashboard";
import EmployeeDashboard from "../pages/employee/Dashboard";
import ClientDashboard from "../pages/client/Dashboard";
import ServicePage from "../pages/services/ServicePage";

export default function AppRoutes() {
  return (
    <Routes>
      {/* Authentication */}
      <Route path="/" element={<Login />} />

      {/* Admin */}
      <Route path="/admin/dashboard" element={<AdminDashboard />} />
      <Route
        path="/services/:serviceSlug"
        element={<ServicePage category="digital" />}
      />
      <Route
        path="/career/:serviceSlug"
        element={<ServicePage category="career" />}
      />
      <Route
        path="/admin/:sectionSlug"
        element={<ServicePage category="management" />}
      />

      {/* Employee */}
      <Route
        path="/employee/dashboard"
        element={<EmployeeDashboard />}
      />

      {/* Client */}
      <Route
        path="/client/dashboard"
        element={<ClientDashboard />}
      />

      {/* Redirect */}
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
}
