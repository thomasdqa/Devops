function remove_user_admin(UserId) {
    fetch("/remove-user-admin", {
      method: "POST",
      body: JSON.stringify({ UserId: UserId }),
    }).then((_res) => {
      window.location.href = "/adminPrivileges";
    });
  }