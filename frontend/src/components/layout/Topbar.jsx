import { FaBell, FaCalendarAlt, FaSearch } from "react-icons/fa";
import "./Topbar.css";

export default function Topbar({ role = "Admin", roleLabel = "Administrator" }) {
  const today = new Date().toLocaleDateString("en-IN", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
  const initials = role
    .split(" ")
    .map((part) => part[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();

  return (
    <header className="topbar">
      <div className="topbar-left">
        <span>{role}</span>
        <strong>/</strong>
        <h2>Dashboard</h2>
      </div>

      <div className="topbar-center">
        <div className="search-box">
          <FaSearch className="search-icon" />
          <input
            type="text"
            placeholder="Search projects, clients..."
          />
        </div>
      </div>

      <div className="topbar-right">
        <div className="date-chip">
          <FaCalendarAlt />
          <span>{today}</span>
        </div>

        <button className="icon-btn">
          <FaBell />
        </button>

        <div className="profile-box">
          <div className="avatar">{initials}</div>

          <div>
            <h4>{role}</h4>
            <span>{roleLabel}</span>
          </div>
        </div>
      </div>
    </header>
  );
}
