import {
  FaTachometerAlt,
  FaGlobe,
  FaUserTie,
  FaProjectDiagram,
  FaTasks,
  FaFileAlt,
  FaChartBar,
  FaCog,
  FaSignOutAlt,
  FaUserShield,
} from "react-icons/fa";
import { NavLink } from "react-router-dom";

import "./Sidebar.css";

const digitalServices = [
  { label: "Website Development", to: "/services/website-development" },
  { label: "Web Applications", to: "/services/web-applications" },
  { label: "SEO", to: "/services/seo" },
  { label: "Maintenance", to: "/services/maintenance" },
];

const dashboardItems = [
  { label: "Clients", to: "/admin/clients" },
  { label: "Employees", to: "/admin/employees" },
];

const careerServices = [
  { label: "Resume Builder", to: "/career/resume-builder" },
  { label: "Profiles", to: "/career/profiles" },
  { label: "ATS Resume Review", to: "/career/ats-resume-review" },
  { label: "Interview Prep", to: "/career/interview-prep" },
];

const managementItems = [
  { label: "Projects", to: "/admin/projects", icon: FaProjectDiagram },
  { label: "Tasks", to: "/admin/tasks", icon: FaTasks },
  { label: "Documents", to: "/admin/documents", icon: FaFileAlt },
  { label: "Reports", to: "/admin/reports", icon: FaChartBar },
  { label: "Settings", to: "/admin/settings", icon: FaCog },
];

const menuClassName = ({ isActive }) => (
  isActive ? "menu-item active" : "menu-item"
);

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <h2>ALCN</h2>
        <p>Connect - Innovate - Elevate</p>
      </div>

      <nav className="sidebar-nav">
        <div className="menu-section">
          <span className="menu-title">MAIN</span>

          <NavLink to="/admin/dashboard" className={menuClassName}>
            <FaTachometerAlt />
            <span>Dashboard</span>
          </NavLink>
        </div>

        <div className="menu-section">
          <span className="menu-title">DASHBOARDS</span>

          {dashboardItems.map((item) => (
            <NavLink className={menuClassName} key={item.to} to={item.to}>
              <FaUserShield />
              <span>{item.label}</span>
            </NavLink>
          ))}
        </div>

        <div className="menu-section">
          <span className="menu-title">DIGITAL SERVICES</span>

          {digitalServices.map((item) => (
            <NavLink className={menuClassName} key={item.to} to={item.to}>
              <FaGlobe />
              <span>{item.label}</span>
            </NavLink>
          ))}
        </div>

        <div className="menu-section">
          <span className="menu-title">CAREER SERVICES</span>

          {careerServices.map((item) => (
            <NavLink className={menuClassName} key={item.to} to={item.to}>
              <FaUserTie />
              <span>{item.label}</span>
            </NavLink>
          ))}
        </div>

        <div className="menu-section">
          <span className="menu-title">MANAGEMENT</span>

          {managementItems.map((item) => {
            const Icon = item.icon;

            return (
              <NavLink className={menuClassName} key={item.to} to={item.to}>
                <Icon />
                <span>{item.label}</span>
              </NavLink>
            );
          })}
        </div>
      </nav>

      <div className="sidebar-footer">
        <NavLink className="logout-btn" to="/">
          <FaSignOutAlt />
          <span>Logout</span>
        </NavLink>
      </div>
    </aside>
  );
};

export default Sidebar;
