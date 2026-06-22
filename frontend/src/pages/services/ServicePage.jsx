import { useMemo, useState } from "react";
import { Navigate, useParams } from "react-router-dom";
import { FaBan, FaEdit, FaTrash } from "react-icons/fa";

import DashboardLayout from "../../components/layout/DashboardLayout";

const serviceContent = {
  digital: {
    "website-development": {
      title: "Website Development",
      subtitle: "Plan, build, and launch responsive business websites.",
      metrics: [
        ["Active Builds", "14"],
        ["Awaiting Content", "6"],
        ["Ready to Launch", "3"],
        ["Completed", "58"],
      ],
      rows: [
        ["Business Website", "ABC Pvt Ltd", "In Progress"],
        ["Portfolio Refresh", "Design Studio", "Review"],
        ["Landing Page", "ALCN Careers", "Ready"],
      ],
    },
    "web-applications": {
      title: "Web Applications",
      subtitle: "Track custom portals, dashboards, and internal tools.",
      metrics: [
        ["Active Apps", "9"],
        ["Feature Requests", "27"],
        ["QA Review", "5"],
        ["Released", "31"],
      ],
      rows: [
        ["Client Portal", "FinEdge", "Development"],
        ["Inventory Dashboard", "Retail Hub", "QA"],
        ["Booking System", "Travel Desk", "Planning"],
      ],
    },
    seo: {
      title: "SEO",
      subtitle: "Monitor audits, keyword work, and optimization progress.",
      metrics: [
        ["Campaigns", "16"],
        ["Audits Due", "4"],
        ["Keywords Tracked", "240"],
        ["Wins This Month", "38"],
      ],
      rows: [
        ["Technical Audit", "ABC Pvt Ltd", "In Progress"],
        ["Local SEO", "Cafe Nine", "Active"],
        ["Content Plan", "EduPath", "Drafting"],
      ],
    },
    maintenance: {
      title: "Maintenance",
      subtitle: "Manage updates, fixes, backups, and care plans.",
      metrics: [
        ["Care Plans", "22"],
        ["Open Fixes", "8"],
        ["Updates Done", "46"],
        ["Backups Verified", "19"],
      ],
      rows: [
        ["Plugin Updates", "XYZ Store", "Scheduled"],
        ["Speed Fixes", "ABC Pvt Ltd", "In Progress"],
        ["Monthly Backup", "Health Plus", "Done"],
      ],
    },
  },
  career: {
    "resume-builder": {
      title: "Resume Builder",
      subtitle: "Create polished resumes for students and professionals.",
      metrics: [
        ["Drafts", "18"],
        ["Under Review", "7"],
        ["Finalized", "42"],
        ["Templates", "12"],
      ],
      rows: [
        ["Software Resume", "Rahul", "Review"],
        ["MBA Resume", "Priya", "Drafting"],
        ["Fresher Resume", "Arun", "Final"],
      ],
    },
    profiles: {
      title: "Profiles",
      subtitle: "Create and optimize Naukri, LinkedIn, and career portal profiles.",
      metrics: [
        ["Naukri Profiles", "32"],
        ["LinkedIn Profiles", "28"],
        ["Portal Updates", "14"],
        ["Ready to Share", "9"],
      ],
      rows: [
        ["Naukri Profile", "Rahul", "Keyword Update"],
        ["LinkedIn Profile", "Priya", "Banner Review"],
        ["Indeed Profile", "Arun", "Ready"],
      ],
    },
    "ats-resume-review": {
      title: "ATS Resume Review",
      subtitle: "Check resume quality, keywords, and screening readiness.",
      metrics: [
        ["Reviews", "21"],
        ["Pending", "5"],
        ["High Score", "13"],
        ["Revisions", "9"],
      ],
      rows: [
        ["Data Analyst Resume", "Meera", "Scored"],
        ["Java Developer Resume", "Kiran", "Pending"],
        ["HR Resume", "Anita", "Revision"],
      ],
    },
    "interview-prep": {
      title: "Interview Prep",
      subtitle: "Schedule mock interviews and coaching sessions.",
      metrics: [
        ["Sessions", "15"],
        ["Scheduled", "6"],
        ["Completed", "33"],
        ["Feedback Due", "4"],
      ],
      rows: [
        ["Frontend Mock", "Rahul", "Scheduled"],
        ["HR Round", "Priya", "Completed"],
        ["System Design", "Neha", "Planning"],
      ],
    },
  },
  management: {
    projects: {
      title: "Projects",
      subtitle: "Review project delivery, ownership, and current status.",
      metrics: [
        ["All Projects", "2,847"],
        ["Active Projects", "42"],
        ["Pending Review", "16"],
        ["Completed", "1,932"],
      ],
      rows: [
        ["Business Website", "ABC Pvt Ltd", "In Progress"],
        ["E-Commerce Portal", "XYZ Store", "Pending"],
        ["Client Portal", "FinEdge", "QA Review"],
        ["SEO Campaign", "Cafe Nine", "Active"],
      ],
    },
    tasks: {
      title: "Tasks",
      subtitle: "Track assigned work, deadlines, and completion.",
      metrics: [
        ["All Tasks", "324"],
        ["Active Tasks", "29"],
        ["Due Today", "6"],
        ["Completed", "241"],
      ],
      rows: [
        ["Homepage UI Fix", "ALCN Team", "Due Today"],
        ["Profile Keyword Update", "Rahul", "In Progress"],
        ["Resume Final Review", "Priya", "Review"],
        ["SEO Audit Report", "Cafe Nine", "Pending"],
      ],
    },
    clients: {
      title: "Clients",
      subtitle: "Manage client accounts, contacts, and engagement.",
      metrics: [
        ["All Clients", "128"],
        ["Active Clients", "94"],
        ["New Leads", "21"],
        ["Restricted", "3"],
      ],
      rows: [
        ["ABC Pvt Ltd", "Meena Sharma", "Active"],
        ["XYZ Store", "Ravi Kumar", "Project Pending"],
        ["FinEdge", "Anita Rao", "Active"],
        ["Cafe Nine", "Suresh Nair", "SEO Active"],
      ],
    },
    employees: {
      title: "Employees",
      subtitle: "View team members, roles, and workload.",
      metrics: [
        ["All Employees", "18"],
        ["Available", "11"],
        ["On Projects", "7"],
        ["Access Review", "2"],
      ],
      rows: [
        ["Asha R", "Frontend Developer", "Available"],
        ["Kiran P", "SEO Specialist", "Assigned"],
        ["Neha S", "Resume Expert", "Assigned"],
        ["Arun M", "Project Coordinator", "Available"],
      ],
    },
    documents: {
      title: "Documents",
      subtitle: "Organize client files, project assets, and records.",
      metrics: [
        ["All Documents", "642"],
        ["Shared", "214"],
        ["Needs Review", "18"],
        ["Archived", "92"],
      ],
      rows: [
        ["Project Proposal", "ABC Pvt Ltd", "Shared"],
        ["Resume Draft", "Rahul", "Review"],
        ["SEO Audit PDF", "Cafe Nine", "Ready"],
        ["Invoice June", "XYZ Store", "Archived"],
      ],
    },
    reports: {
      title: "Reports",
      subtitle: "Export and inspect operational reporting data.",
      metrics: [
        ["All Reports", "76"],
        ["Revenue Reports", "12"],
        ["Career Reports", "18"],
        ["Exports Ready", "9"],
      ],
      rows: [
        ["Monthly Revenue", "Admin", "Ready"],
        ["Career Revenue", "Finance", "Ready"],
        ["Project Summary", "Operations", "Draft"],
        ["Client Activity", "Admin", "Ready"],
      ],
    },
    settings: {
      title: "Settings",
      subtitle: "Configure account, workflow, and platform preferences.",
      metrics: [
        ["System Rules", "14"],
        ["Role Access", "6"],
        ["Pending Changes", "2"],
        ["Blocked Access", "3"],
      ],
      rows: [
        ["Admin Permissions", "System", "Active"],
        ["Employee Access", "HR", "Review"],
        ["Client Portal", "Support", "Active"],
        ["Report Exports", "Finance", "Restricted"],
      ],
    },
  },
};

const fallbackMetrics = [
  ["Open Items", "12"],
  ["In Progress", "8"],
  ["Completed", "34"],
  ["Needs Review", "5"],
];

const fallbackRows = [
  ["Current Work", "ALCN", "Active"],
  ["Pending Review", "Operations", "Review"],
  ["Next Milestone", "Team", "Planned"],
];

export default function ServicePage({ category }) {
  const { serviceSlug, sectionSlug } = useParams();
  const slug = serviceSlug || sectionSlug;
  const content = serviceContent[category]?.[slug];

  if (!content) {
    return <Navigate to="/admin/dashboard" replace />;
  }

  return (
    <ServicePageContent
      category={category}
      content={content}
      key={`${category}-${slug}`}
    />
  );
}

function ServicePageContent({ content }) {
  const metrics = content.metrics || fallbackMetrics;
  const initialRows = useMemo(
    () => (content?.rows || fallbackRows).map(([item, owner, status]) => ({
      item,
      owner,
      status,
    })),
    [content]
  );
  const [records, setRecords] = useState(initialRows);
  const [editingRecord, setEditingRecord] = useState(null);
  const [notice, setNotice] = useState("");
  const [activeMetric, setActiveMetric] = useState(metrics[0]?.[0] || "All");
  const metricMatchers = {
    "Active Clients": /active/i,
    "New Leads": /lead|new|pending/i,
    Restricted: /restricted|denied/i,
    Available: /available/i,
    "On Projects": /assigned|project/i,
    "Access Review": /review|denied|restricted/i,
  };

  const filterRecords = (metricTitle, currentRecords) => {
    const title = metricTitle.toLowerCase();
    const exactMatcher = metricMatchers[metricTitle];

    if (exactMatcher) {
      return currentRecords.filter((record) => exactMatcher.test(record.status));
    }

    if (title.includes("all") || title.includes("total") || title.includes("campaigns")) {
      return currentRecords;
    }

    if (title.includes("active") || title.includes("available") || title.includes("shared")) {
      return currentRecords.filter((record) => (
        /active|progress|development|available|assigned|shared|qa/i.test(record.status)
      ));
    }

    if (
      title.includes("new") ||
      title.includes("lead") ||
      title.includes("pending") ||
      title.includes("review") ||
      title.includes("due") ||
      title.includes("awaiting") ||
      title.includes("needs")
    ) {
      return currentRecords.filter((record) => (
        /lead|new|pending|review|due|draft|scheduled/i.test(record.status)
      ));
    }

    if (
      title.includes("completed") ||
      title.includes("ready") ||
      title.includes("released") ||
      title.includes("final") ||
      title.includes("archived") ||
      title.includes("exports")
    ) {
      return currentRecords.filter((record) => (
        /completed|ready|final|done|archived|scored/i.test(record.status)
      ));
    }

    if (title.includes("restricted") || title.includes("blocked")) {
      return currentRecords.filter((record) => (
        /restricted|denied/i.test(record.status)
      ));
    }

    return currentRecords;
  };
  const visibleRecords = filterRecords(activeMetric, records);
  const computedMetrics = metrics.map(([title, value]) => {
    const titleLower = title.toLowerCase();
    const shouldUseRecordCount = (
      titleLower.includes("all") ||
      titleLower.includes("total") ||
      titleLower.includes("active") ||
      titleLower.includes("pending") ||
      titleLower.includes("new") ||
      titleLower.includes("lead") ||
      titleLower.includes("review") ||
      titleLower.includes("completed") ||
      titleLower.includes("restricted") ||
      titleLower.includes("blocked") ||
      titleLower.includes("available") ||
      titleLower.includes("shared") ||
      titleLower.includes("ready") ||
      titleLower.includes("due") ||
      titleLower.includes("needs") ||
      titleLower.includes("awaiting")
    );

    return [
      title,
      shouldUseRecordCount
        ? String(filterRecords(title, records).length)
        : value,
    ];
  });

  const selectMetric = (title) => {
    setActiveMetric(title);
    setNotice(`Showing ${title.toLowerCase()} records.`);
  };

  const updateRecord = (event) => {
    event.preventDefault();

    if (editingRecord.mode === "add") {
      const newRecord = {
        item: editingRecord.item.trim() || "New Record",
        owner: editingRecord.owner.trim() || "Unassigned",
        status: editingRecord.status.trim() || "Active",
      };

      setRecords((currentRecords) => [newRecord, ...currentRecords]);
      setActiveMetric("All");
      setNotice(`${newRecord.item} added.`);
      setEditingRecord(null);
      return;
    }

    setRecords((currentRecords) => currentRecords.map((record) => (
      record.item === editingRecord.originalItem
        ? {
          item: editingRecord.item,
          owner: editingRecord.owner,
          status: editingRecord.status,
        }
        : record
    )));
    setNotice(`${editingRecord.item} details updated.`);
    setEditingRecord(null);
  };

  const removeRecord = (recordToRemove) => {
    setRecords((currentRecords) => currentRecords.filter(
      (record) => record.item !== recordToRemove.item
    ));
    setNotice(`${recordToRemove.item} removed from the list.`);
  };

  const denyAccess = (recordToDeny) => {
    setRecords((currentRecords) => currentRecords.map((record) => (
      record.item === recordToDeny.item
        ? { ...record, status: "Access Denied" }
        : record
    )));
    setNotice(`Access denied for ${recordToDeny.item}.`);
  };

  const openAddRecord = () => {
    setEditingRecord({
      item: "",
      mode: "add",
      originalItem: "",
      owner: "",
      status: "Active",
    });
  };

  return (
    <DashboardLayout>
      <div className="page-heading-row">
        <div>
          <h1 className="page-title">{content.title}</h1>
          <p className="page-subtitle">{content.subtitle}</p>
        </div>

        <button className="add-record-btn" onClick={openAddRecord} type="button">
          + Add Record
        </button>
      </div>

      <div className="stats-grid">
        {computedMetrics.map(([title, value]) => (
          <button
            className={activeMetric === title ? "stat-card stat-card-button active" : "stat-card stat-card-button"}
            key={title}
            onClick={() => selectMetric(title)}
            type="button"
          >
            <h4>{title}</h4>
            <h2>{value}</h2>
          </button>
        ))}
      </div>

      <div className="table-card">
        <div className="table-heading-row">
          <h3>Recent Activity</h3>
          {notice && <span className="action-notice">{notice}</span>}
        </div>

        <table className="data-table">
          <thead>
            <tr>
              <th>Item</th>
              <th>Owner</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {visibleRecords.map((record) => (
              <tr key={`${record.item}-${record.owner}`}>
                <td>{record.item}</td>
                <td>{record.owner}</td>
                <td>
                  <span className={record.status === "Access Denied" ? "status denied" : "status"}>
                    {record.status}
                  </span>
                </td>
                <td>
                  <div className="record-actions">
                    <button
                      aria-label={`Edit ${record.item}`}
                      className="action-icon edit"
                      onClick={() => setEditingRecord({
                        ...record,
                        originalItem: record.item,
                      })}
                      title="Edit details"
                      type="button"
                    >
                      <FaEdit />
                    </button>
                    <button
                      aria-label={`Remove ${record.item}`}
                      className="action-icon remove"
                      onClick={() => removeRecord(record)}
                      title="Remove"
                      type="button"
                    >
                      <FaTrash />
                    </button>
                    <button
                      aria-label={`Deny access for ${record.item}`}
                      className="action-icon deny"
                      onClick={() => denyAccess(record)}
                      title="Deny access"
                      type="button"
                    >
                      <FaBan />
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {editingRecord && (
        <div className="modal-backdrop">
          <form className="edit-modal" onSubmit={updateRecord}>
            <div className="modal-heading">
              <h3>{editingRecord.mode === "add" ? "Add Record" : "Edit Details"}</h3>
              <button
                aria-label="Close edit form"
                onClick={() => setEditingRecord(null)}
                type="button"
              >
                X
              </button>
            </div>

            <label>
              Item
              <input
                value={editingRecord.item}
                onChange={(event) => setEditingRecord({
                  ...editingRecord,
                  item: event.target.value,
                })}
              />
            </label>

            <label>
              Owner
              <input
                value={editingRecord.owner}
                onChange={(event) => setEditingRecord({
                  ...editingRecord,
                  owner: event.target.value,
                })}
              />
            </label>

            <label>
              Status
              <input
                value={editingRecord.status}
                onChange={(event) => setEditingRecord({
                  ...editingRecord,
                  status: event.target.value,
                })}
              />
            </label>

            <div className="modal-actions">
              <button
                className="secondary-action"
                onClick={() => setEditingRecord(null)}
                type="button"
              >
                Cancel
              </button>
              <button className="primary-action" type="submit">
                Save
              </button>
            </div>
          </form>
        </div>
      )}
    </DashboardLayout>
  );
}
