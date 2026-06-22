import Sidebar from "./Sidebar";
import Topbar from "./Topbar";
import "./DashboardLayout.css";

export default function DashboardLayout({ children, role = "Admin", roleLabel = "Administrator" }) {
  return (
    <div className="dashboard-wrapper">
      <Sidebar />

      <div className="dashboard-main">
        <Topbar role={role} roleLabel={roleLabel} />

        <div className="dashboard-content">
          {children}
        </div>
      </div>
    </div>
  );
}
