function buildFilters(category, filters){
	var filter_selector = document.getElementById("filter-selector");
	if(category == "default"){
		button.disabled = true;
		filter_selector.disabled = true;
	}
	else{
		var filter_list = filters[category];
		for (var i = 0; i < filter_list.length; i++) {
            var currentFilter = filter_list[i];
            var option = document.createElement("option")
            /* TODO: Set value so correct info can be displayed for that filter
            EX: option.setAttribute("value", value);
            */
            option.setAttribute("value", currentFilter);
            var text = document.createTextNode(currentFilter);
            option.appendChild(text);

            filter_selector.appendChild(option)
        }
		filter_selector.disabled = false;
	}
	console.log("build ran");
}

function changeButtonStatus(filter_selected){
	var button = document.getElementById("button")
	if(filter_selected == "default"){
		button.disabled = true;
	}
	else{
		button.disabled = false;
	}
	console.log("button status ran");
}