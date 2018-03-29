function buildFilters(category, filters){
	var filter_selector = document.getElementByID("filter-selector");
	if(category == "default"){
		button.disabled = true;
		filter_selector.disabled = true;
	}
	else{
		/* TODO: add statement for choosing different filter sets*/
		for (var i = 0; i < filters.length; i++) {
            var currentFilter = filters[i];
            var option = document.createElement("option")
            /* TODO: Set value so correct info can be displayed for that filter
            EX: option.setAttribute("value", value);
            */
            var text = document.createTextNode(currentFilter);
            option.appendChild(text);

            filter_selector.appendChild(option)
        }
		filter_selector.disabled = false;
	}
	console.log("build ran");
}

function changeButtonStatus(filter_selected){
	var button = document.getElementByID("button")
	if(filter_selected == "default"){
		button.disabled = true;
	}
	else{
		button.disabled = false;
	}
	console.log("button status ran");
}