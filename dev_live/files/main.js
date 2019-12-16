$(function(){
	//左下角展开关闭
	$("#open-close").click(function(){
		if($("#main-sidebar").hasClass("sidebar-collapsed") && $("#bce-content").hasClass("sidebar-collapsed")){
			$("#main-sidebar").removeClass("sidebar-collapsed");
			$("#main-sidebar").addClass("sidebar-expanded");
			$("#bce-content").removeClass("sidebar-collapsed");
			$("#bce-content").addClass("sidebar-expanded");
		}else{
			$("#main-sidebar").removeClass("sidebar-expanded");
			$("#main-sidebar").addClass("sidebar-collapsed");
			$("#bce-content").removeClass("sidebar-expanded");
			$("#bce-content").addClass("sidebar-collapsed");
		}
	});
});



$("#header").load("./header.html");
//$("#main-sidebar").load("./side.html");

