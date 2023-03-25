function serviceId_request2(service_requestId2) {
    fetch("/service-id_request2", {
      method: "POST",
      body: JSON.stringify({ service_requestId2: service_requestId2 }),
    }).then((_res) => {
      window.location.href = "/admin/";
    });
  }