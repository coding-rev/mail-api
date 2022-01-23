submitContactFormThroughApi(){
	body={
		"company_name":document.querySelector("#mailCompanyName").value,
		"company_email":document.querySelector("#mailCompanyEmail").value,
		"name":document.querySelector("#mailName").value,
		"email":document.querySelector("#mailEmail").value,
		"message":document.querySelector("#mailMessage").value,
	};
	const headers = {
		"Content-Type": "application/json",
		"Accept": "application/json",
	};
	fetch("https://manuel-mailapi.herokuapp.com/api/", {
			method: "POST",
			headers,
			body: JSON.stringify(body),
	})
	.then((response)=>{
		alert("Sent")
	})
	.catch((e)=>{
		alert("Couldn't send mail.")
	})
};