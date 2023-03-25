function serviceId_request(service_requestId) {
    fetch("/service-id_request", {
      method: "POST",
      body: JSON.stringify({ service_requestId: service_requestId }),
    }).then((_res) => {
      window.location.href = "/admin/";
    });
  }