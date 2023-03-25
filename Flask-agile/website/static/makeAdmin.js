function make_user_admin(UserId) {
    fetch("/make-user-admin", {
      method: "POST",
      body: JSON.stringify({ UserId: UserId }),
    }).then((_res) => {
      window.location.href = "/adminPrivileges";
    });
  }