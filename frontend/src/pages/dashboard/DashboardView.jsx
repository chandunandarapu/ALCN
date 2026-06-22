import { useState } from "react";
import { NavLink } from "react-router-dom";

import DashboardLayout from "../../components/layout/DashboardLayout";

const dashboardData = {
  admin: {
    role: "Admin",
    roleLabel: "Administrator",
    title: "Dashboard",
    subtitle: "Welcome back, Super Admin - here is today's overview",
    cards: [
      { title: "Total Clients", value: "128", trend: "12% this month", to: "/admin/clients" },
      { title: "Total Projects", value: "2,847", trend: "8% this month", to: "/admin/projects" },
      { title: "Active Projects", value: "42", trend: "5% this month", to: "/admin/projects" },
      { title: "Revenue", value: "24.8L", trend: "15% this month", to: "/admin/reports" },
    ],
    careerCards: [
      { title: "Total Resumes", value: "214", trend: "18 new this month", to: "/career/resume-builder" },
      { title: "Total Profiles", value: "87", trend: "Naukri and LinkedIn", to: "/career/profiles" },
      { title: "Active Tasks", value: "29", trend: "6 due today", to: "/admin/tasks" },
      { title: "Career Revenue", value: "4.6L", trend: "11% this month", to: "/admin/reports" },
    ],
    bars: [62, 56, 74, 70, 88],
    targets: [58, 60, 68, 66, 72],
    donut: [
      ["Website Development", "35%"],
      ["Web Applications", "28%"],
      ["Career Services", "22%"],
      ["Maintenance", "15%"],
    ],
    rows: [
      ["Business Website", "ABC Pvt Ltd", "In Progress"],
      ["Resume Review", "Rahul", "Completed"],
      ["E-Commerce Portal", "XYZ Store", "Pending"],
    ],
  },
  employee: {
    role: "Employee",
    roleLabel: "Team Member",
    title: "Dashboard",
    subtitle: "Welcome back, Employee - here is your work performance",
    cards: [
      { title: "Assigned Projects", value: "12", trend: "3 new this month", to: "/admin/projects" },
      { title: "Pending Tasks", value: "7", trend: "2 due today", to: "/admin/tasks" },
      { title: "Completed Tasks", value: "35", trend: "9% this month", to: "/admin/tasks" },
      { title: "Review Score", value: "94%", trend: "4% improvement", to: "/admin/reports" },
    ],
    careerCards: [
      { title: "Total Resumes", value: "48", trend: "Assigned to you", to: "/career/resume-builder" },
      { title: "Total Profiles", value: "19", trend: "Profile updates", to: "/career/profiles" },
      { title: "Active Tasks", value: "7", trend: "2 due today", to: "/admin/tasks" },
      { title: "Career Revenue", value: "82K", trend: "Handled work", to: "/admin/reports" },
    ],
    bars: [48, 72, 58, 80, 66],
    targets: [52, 68, 62, 74, 70],
    donut: [
      ["Development", "40%"],
      ["Client Changes", "25%"],
      ["QA Fixes", "20%"],
      ["Reviews", "15%"],
    ],
    rows: [
      ["Homepage Update", "ALCN", "Due Today"],
      ["SEO Fixes", "Cafe Nine", "In Progress"],
      ["Resume Draft", "Priya", "Review"],
    ],
  },
  client: {
    role: "Client",
    roleLabel: "Customer",
    title: "Dashboard",
    subtitle: "Welcome back, Client - here is your project visibility",
    cards: [
      { title: "Active Projects", value: "3", trend: "1 in review", to: "/admin/projects" },
      { title: "Career Requests", value: "1", trend: "Draft ready", to: "/career/resume-builder" },
      { title: "Documents", value: "14", trend: "4 updated", to: "/admin/documents" },
      { title: "Support Tickets", value: "2", trend: "1 resolved", to: "/admin/tasks" },
    ],
    careerCards: [
      { title: "Total Resumes", value: "3", trend: "1 under review", to: "/career/resume-builder" },
      { title: "Total Profiles", value: "2", trend: "Naukri and LinkedIn", to: "/career/profiles" },
      { title: "Active Tasks", value: "4", trend: "Client action needed", to: "/admin/tasks" },
      { title: "Career Revenue", value: "18K", trend: "Current package", to: "/admin/reports" },
    ],
    bars: [55, 60, 72, 64, 78],
    targets: [50, 62, 68, 70, 75],
    donut: [
      ["Website", "45%"],
      ["SEO", "20%"],
      ["Documents", "20%"],
      ["Support", "15%"],
    ],
    rows: [
      ["Business Website", "ALCN Team", "In Progress"],
      ["Content Upload", "Client", "Pending"],
      ["SEO Audit", "ALCN Team", "Completed"],
    ],
  },
};

const months = ["Jan", "Feb", "Mar", "Apr", "May"];
const donutColors = ["#2447b8", "#22a65a", "#df860d", "#7c3aed"];

const toPercentNumber = (value) => Number(value.replace("%", ""));
const polarToCartesian = (center, radius, angleInDegrees) => {
  const angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180;

  return {
    x: center + radius * Math.cos(angleInRadians),
    y: center + radius * Math.sin(angleInRadians),
  };
};
const describeDonutSegment = (startPercent, percent) => {
  const center = 50;
  const outerRadius = 45;
  const innerRadius = 27;
  const startAngle = startPercent * 3.6;
  const endAngle = (startPercent + percent) * 3.6;
  const largeArcFlag = percent > 50 ? 1 : 0;
  const outerStart = polarToCartesian(center, outerRadius, endAngle);
  const outerEnd = polarToCartesian(center, outerRadius, startAngle);
  const innerStart = polarToCartesian(center, innerRadius, startAngle);
  const innerEnd = polarToCartesian(center, innerRadius, endAngle);

  return [
    `M ${outerStart.x} ${outerStart.y}`,
    `A ${outerRadius} ${outerRadius} 0 ${largeArcFlag} 0 ${outerEnd.x} ${outerEnd.y}`,
    `L ${innerStart.x} ${innerStart.y}`,
    `A ${innerRadius} ${innerRadius} 0 ${largeArcFlag} 1 ${innerEnd.x} ${innerEnd.y}`,
    "Z",
  ].join(" ");
};

export default function DashboardView({ type }) {
  const data = dashboardData[type] || dashboardData.admin;
  const [activeChartDetail, setActiveChartDetail] = useState(null);
  const [activeCategoryDetail, setActiveCategoryDetail] = useState(null);
  const defaultChartDetail = {
    title: "Chart details",
    lines: [
      "Hover a bar or category to see the values.",
      "Click or focus items to keep the detail visible.",
    ],
  };
  const chartDetail = activeChartDetail || defaultChartDetail;
  const categoryDetail = activeCategoryDetail || {
    title: "Category details",
    lines: ["Hover a slice or category row to see its share."],
  };
  const donutSegments = data.donut.reduce((segments, [label, value]) => {
    const percent = toPercentNumber(value);
    const previousOffset = segments.reduce(
      (total, segment) => total + segment.percent,
      0
    );

    return [
      ...segments,
      {
        label,
        offset: previousOffset,
        percent,
        value,
      },
    ];
  }, []);

  return (
    <DashboardLayout role={data.role} roleLabel={data.roleLabel}>
      <section className="dashboard-heading">
        <h1 className="page-title">{data.title}</h1>
        <p className="page-subtitle">{data.subtitle}</p>
      </section>

      <div className="stats-grid">
        {data.cards.map((card) => (
          <NavLink className="stat-card stat-card-link" key={card.title} to={card.to}>
            <h4>{card.title}</h4>
            <h2>{card.value}</h2>
            <span className="trend-pill">+ {card.trend}</span>
          </NavLink>
        ))}
      </div>

      <section className="career-summary">
        <div className="section-heading-row">
          <div>
            <h2>Career Services</h2>
            <p>Resume, profile, task, and revenue visibility</p>
          </div>
        </div>

        <div className="career-card-grid">
          {data.careerCards.map((card) => (
            <NavLink className="career-card" key={card.title} to={card.to}>
              <span>{card.title}</span>
              <strong>{card.value}</strong>
              <small>{card.trend}</small>
            </NavLink>
          ))}
        </div>
      </section>

      <div className="dashboard-panels">
        <section className="chart-card wide">
          <h3>Performance vs Target</h3>
          <div className="chart-detail-box" aria-live="polite">
            <strong>{chartDetail.title}</strong>
            {chartDetail.lines.map((line) => (
              <span key={line}>{line}</span>
            ))}
          </div>

          <div className="bar-chart" aria-label="Performance chart">
            {months.map((month, index) => (
              <div className="bar-group" key={month}>
                <div className="bar-pair">
                  <span
                    aria-label={`${month} performance ${data.bars[index]}`}
                    className="bar actual"
                    onBlur={() => setActiveChartDetail(null)}
                    onClick={() => setActiveChartDetail({
                      title: `${month} performance`,
                      lines: [
                        `Performance: ${data.bars[index]}`,
                        `Target: ${data.targets[index]}`,
                      ],
                    })}
                    onFocus={() => setActiveChartDetail({
                      title: `${month} performance`,
                      lines: [
                        `Performance: ${data.bars[index]}`,
                        `Target: ${data.targets[index]}`,
                      ],
                    })}
                    onMouseEnter={() => setActiveChartDetail({
                      title: `${month} performance`,
                      lines: [
                        `Performance: ${data.bars[index]}`,
                        `Target: ${data.targets[index]}`,
                      ],
                    })}
                    onMouseLeave={() => setActiveChartDetail(null)}
                    role="button"
                    style={{ height: `${data.bars[index]}%` }}
                    tabIndex="0"
                  />
                  <span
                    aria-label={`${month} target ${data.targets[index]}`}
                    className="bar target"
                    onBlur={() => setActiveChartDetail(null)}
                    onClick={() => setActiveChartDetail({
                      title: `${month} target`,
                      lines: [
                        `Target: ${data.targets[index]}`,
                        `Performance: ${data.bars[index]}`,
                      ],
                    })}
                    onFocus={() => setActiveChartDetail({
                      title: `${month} target`,
                      lines: [
                        `Target: ${data.targets[index]}`,
                        `Performance: ${data.bars[index]}`,
                      ],
                    })}
                    onMouseEnter={() => setActiveChartDetail({
                      title: `${month} target`,
                      lines: [
                        `Target: ${data.targets[index]}`,
                        `Performance: ${data.bars[index]}`,
                      ],
                    })}
                    onMouseLeave={() => setActiveChartDetail(null)}
                    role="button"
                    style={{ height: `${data.targets[index]}%` }}
                    tabIndex="0"
                  />
                  <div className="chart-tooltip">
                    <strong>{month}</strong>
                    <span>Performance: {data.bars[index]}</span>
                    <span>Target: {data.targets[index]}</span>
                  </div>
                </div>
                <small>{month}</small>
              </div>
            ))}
          </div>
        </section>

        <section className="chart-card">
          <h3>Work by Category</h3>
          <div className="chart-detail-box compact" aria-live="polite">
            <strong>{categoryDetail.title}</strong>
            {categoryDetail.lines.map((line) => (
              <span key={line}>{line}</span>
            ))}
          </div>

          <div className="donut-wrap">
            <svg
              aria-label="Work by category chart"
              className="donut-svg"
              viewBox="0 0 100 100"
            >
              <circle className="donut-track" cx="50" cy="50" r="45" />

              {donutSegments.map((segment, index) => (
                  <path
                    aria-label={`${segment.label} ${segment.value}`}
                    className="donut-slice"
                    d={describeDonutSegment(segment.offset, segment.percent)}
                    fill={donutColors[index % donutColors.length]}
                    key={segment.label}
                    onBlur={() => setActiveCategoryDetail(null)}
                    onClick={() => setActiveCategoryDetail({
                      title: segment.label,
                      lines: [`Share: ${segment.value}`, "Category workload split"],
                    })}
                    onFocus={() => setActiveCategoryDetail({
                      title: segment.label,
                      lines: [`Share: ${segment.value}`, "Category workload split"],
                    })}
                    onMouseEnter={() => setActiveCategoryDetail({
                      title: segment.label,
                      lines: [`Share: ${segment.value}`, "Category workload split"],
                    })}
                    onMouseLeave={() => setActiveCategoryDetail(null)}
                    role="button"
                    tabIndex="0"
                  />
              ))}
            </svg>

            <div className="donut-center">
              <strong>{categoryDetail.title}</strong>
              <span>{categoryDetail.lines[0]}</span>
            </div>
          </div>

          <div className="legend-list">
            {data.donut.map(([label, value]) => (
              <button
                className="legend-row"
                key={label}
                onBlur={() => setActiveCategoryDetail(null)}
                onClick={() => setActiveCategoryDetail({
                  title: label,
                  lines: [`Share: ${value}`, "Category workload split"],
                })}
                onFocus={() => setActiveCategoryDetail({
                  title: label,
                  lines: [`Share: ${value}`, "Category workload split"],
                })}
                onMouseEnter={() => setActiveCategoryDetail({
                  title: label,
                  lines: [`Share: ${value}`, "Category workload split"],
                })}
                onMouseLeave={() => setActiveCategoryDetail(null)}
                type="button"
              >
                <span>{label}</span>
                <strong>{value}</strong>
                <em>{label}: {value}</em>
              </button>
            ))}
          </div>
        </section>
      </div>

      <div className="table-card">
        <h3>Recent Activity</h3>

        <table className="data-table">
          <thead>
            <tr>
              <th>Work</th>
              <th>Owner</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {data.rows.map(([work, owner, status]) => (
              <tr key={`${work}-${owner}`}>
                <td>{work}</td>
                <td>{owner}</td>
                <td>{status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </DashboardLayout>
  );
}
