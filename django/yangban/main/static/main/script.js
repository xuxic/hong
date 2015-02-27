$(document).ready(function(){
	$("#toupiao1").load("/main/vote");
	$.getJSON("/main/mmmm",function(data){
		console.log(data.length)
		
		for(var i=0;i<data.length;i++){
			var row = "<td>"+data[i].email+"</td>"+"<td>"+data[i].content+"</td>"+"<td>"+data[i].pub_date+"</td>"
			row = "<tr>"+row+"</tr>"
			$("#message").prepend(row);
		}
	});
	$("li").click(function(){
		$("li").removeClass("active");
		$(this).addClass("active");
	});
	$("button").click(function(){
	  $.post("/main/vote",{},
	  function(data,status){
		  $("#toupiao1").text(data);
	  });
  });
});