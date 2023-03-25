function delete_User(UserId) {
    fetch("/delete-user", {
      method: "POST",
      body: JSON.stringify({ UserId: UserId }),
    }).then((_res) => {
      window.location.href = "/adminPrivileges";
    });
  }