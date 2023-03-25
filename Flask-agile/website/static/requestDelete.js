function deleteService_request(service_requestId) {
    fetch("/delete-service_request", {
      method: "POST",
      body: JSON.stringify({ service_requestId: service_requestId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }