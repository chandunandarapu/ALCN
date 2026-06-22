import { useState } from "react";
import { useNavigate } from "react-router-dom";

const demoAccounts = [
  {
    label: "Admin Login",
    email: "admin@alcn.com",
    path: "/admin/dashboard",
    helper: "Full business overview",
  },
  {
    label: "Employee Login",
    email: "employee@alcn.com",
    path: "/employee/dashboard",
    helper: "Task and performance view",
  },
  {
    label: "Client Login",
    email: "client@alcn.com",
    path: "/client/dashboard",
    helper: "Project visibility view",
  },
];

export default function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const routeForEmail = (value) => {
    if (value === "admin@alcn.com") return "/admin/dashboard";
    if (value === "employee@alcn.com") return "/employee/dashboard";
    return "/client/dashboard";
  };

  const login = (e) => {
    e.preventDefault();
    navigate(routeForEmail(email));
  };

  const quickLogin = (account) => {
    setEmail(account.email);
    setPassword("demo123");
    navigate(account.path);
  };

  return (
    <div className="login-page">
      <form onSubmit={login} className="login-card">
        <div className="login-brand">
          <div className="login-logo">A</div>
          <div>
            <h1>ALCN</h1>
            <p>Dashboard access</p>
          </div>
        </div>

        <label>
          Email
          <input
            placeholder="admin@alcn.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>

        <label>
          Password
          <input
            type="password"
            placeholder="Enter password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>

        <button className="primary-login" type="submit">
          Sign In
        </button>

        <div className="demo-login-grid">
          {demoAccounts.map((account) => (
            <button
              className="demo-login"
              key={account.email}
              onClick={() => quickLogin(account)}
              type="button"
            >
              <strong>{account.label}</strong>
              <span>{account.helper}</span>
            </button>
          ))}
        </div>
      </form>
    </div>
  );
}
