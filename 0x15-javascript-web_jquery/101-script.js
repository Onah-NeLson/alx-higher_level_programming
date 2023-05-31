$(document).ready(function () {
	$("#add_item").click(function () {
		$("<li>").text("Item").appendTo("ul.my_list");
	});
	$("#remove_item").click(function () {
		$("ul.my_list li:last-child").remove();
	});
	$("#clear_list").click(function () {
		$("ul.my_list").empty();
	});
});

// a  script that adds, removes and clears LI elements from a list when the user clicks
