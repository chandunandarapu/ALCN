import json
import urllib.request


BASE_URL = "http://127.0.0.1:8000"


def print_section(title):
    print("=" * 60)
    print(title)
    print("=" * 60)


def run_smoke_tests():
    print_section("TEST 1: JWT Authentication")

    data = json.dumps({
        "username": "admin",
        "password": "admin123",
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{BASE_URL}/api/token/",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read())
        access_token = result.get("access", "")
        print("OK Authentication successful")
        print(f"Access Token: {access_token[:50]}...")
        print()

        print_section("TEST 2: Get Users (with authentication)")

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        req = urllib.request.Request(
            f"{BASE_URL}/api/users/",
            headers=headers,
            method="GET",
        )

        response = urllib.request.urlopen(req)
        users = json.loads(response.read())
        user_count = (
            len(users) if isinstance(users, list) else users.get("count", "N/A")
        )
        print("OK Users endpoint working")
        print(f"Number of users: {user_count}")
        print()

    except Exception as exc:
        print(f"ERROR: {exc}")

    print_section("TEST 3: Swagger UI Documentation")

    try:
        urllib.request.urlopen(f"{BASE_URL}/swagger/")
        print(f"OK Swagger UI is accessible at {BASE_URL}/swagger/")
    except Exception as exc:
        print(f"ERROR: {exc}")

    print_section("TEST 4: Django Admin Interface")

    try:
        urllib.request.urlopen(f"{BASE_URL}/admin/")
        print(f"OK Admin interface is accessible at {BASE_URL}/admin/")
        print("  Login with: admin / admin123")
    except Exception as exc:
        print(f"ERROR: {exc}")

    print()
    print_section("BACKEND STATUS: SMOKE TESTS COMPLETE")


if __name__ == "__main__":
    run_smoke_tests()
