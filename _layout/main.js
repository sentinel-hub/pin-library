var isSearchDisplayed = false;

function toggleSearch() {
	isSearchDisplayed = !isSearchDisplayed;
	document.getElementById("sidebar-search").className = isSearchDisplayed ? 'visible' : 'hidden';
	if (!isSearchDisplayed) {
		document.getElementById("search-box").value = '';
	}
	else {
		document.getElementById("search-box").focus();
	}
	performSearch('');
}

function searchKeyDown(searchElement) {
	if (event.key === 'Enter') {
		performSearch(searchElement.value);        
    }
}

function performSearch(searchValue) {
	if (typeof groups !== 'undefined') {
		performPinsSearch(searchValue);
	}
	if (typeof texts !== 'undefined') {
		performThemeSearch(searchValue);
	}
}

function performThemeSearch(searchValue) {
	for (var themeId in texts) {
		var themeContainer = document.getElementById(themeId);
		if (themeContainer) {
			var themeText = texts[themeId];
			themeContainer.style.display = stringMatch(themeText, searchValue) ? 'inline-block' : 'none';
		}
	}
}

function performPinsSearch(searchValue) {
	for (var groupId in groups) {
		var group = groups[groupId];
		var pins = group['pins'];
		
		for (var pinIndex in pins) {
			var pin = pins[pinIndex];
			pin['visible'] = (stringMatch(pin['title'], searchValue) || stringMatch(pin['description'], searchValue)) ? 'true' : 'false';
		}
		
		var currIndex = 0;
		if (pins[0]['visible'] != 'true') {
			currIndex = getNextVisiblePin(groupId, currIndex);
		}
		updatePin(groupId, group, currIndex);
	}
}

function stringMatch(haystack, needle) {
	if (!needle) {
		return true;
	}
	if (!haystack) {
		return false;
	}
	
	haystack = haystack.toLowerCase();
	var tokens = needle.toLowerCase().split(' ');
	for (var i in tokens) {
		var token = tokens[i];
		if ((token.length > 0) && !haystack.includes(token)) {
			return false;
		}
	}
	return true;
}

function pinLeft(groupId) {
	var group = groups[groupId];
	var currIndex = group['index']
	if (currIndex == undefined) {
		currIndex = 0;
	}
	currIndex = getPrevVisiblePin(groupId, currIndex)
	updatePin(groupId, group, currIndex);
}

function pinRight(groupId) {
	var group = groups[groupId];
	var currIndex = group['index']
	if (currIndex == undefined) {
		currIndex = 0;
	}
	currIndex = getNextVisiblePin(groupId, currIndex)
	updatePin(groupId, group, currIndex);
}

function getGroupPinsCount(groupId) {
	var count = 0;
	var pins = groups[groupId]['pins'];
	for (var pinIndex in pins) {
		var pin = pins[pinIndex];
		if (pin['visible'] == 'true') {
			count++;
		}
	}
	return count;
}

function getPrevVisiblePin(groupId, currIndex) {
	var pins = groups[groupId]['pins'];
	while (currIndex > 0) {
		currIndex--;
		if (pins[currIndex]['visible'] == 'true') {
			return currIndex;
		}
	}
	return -1;
}

function getNextVisiblePin(groupId, currIndex) {
	var pins = groups[groupId]['pins'];
	while (currIndex < pins.length - 1) {
		currIndex++;
		if (pins[currIndex]['visible'] == 'true') {
			return currIndex;
		}
	}
	return -1;
}

function updatePin(groupId, group, currIndex) {
	if (currIndex >= 0) {
		group['index'] = currIndex;
	}
	else {
		currIndex = group['index']; 
	}
	
	var pinCount = getGroupPinsCount(groupId);
	document.getElementById(groupId + '-left').style.display = (getPrevVisiblePin(groupId, currIndex) >= 0) ? 'block' : 'none';
	document.getElementById(groupId + '-right').style.display = (getNextVisiblePin(groupId, currIndex) >= 0) ? 'block' : 'none';
	
	var pins = group['pins'];
	var pin = pins[currIndex];
	
	document.getElementById(groupId + '-container').style.display = (pinCount > 0) ? 'block' : 'none';
	document.getElementById(groupId + '-title').innerHTML = pin['title'];
	document.getElementById(groupId + '-image-path').src = pin['thumbnail_path'];
	document.getElementById(groupId + '-date').innerHTML = pin['date'];
	document.getElementById(groupId + '-type').innerHTML = pin['type'];
	document.getElementById(groupId + '-eob').href = pin['eob_url'];
	document.getElementById(groupId + '-eob').style.display = pin['eob_url'] ? 'block' : 'none';
	document.getElementById(groupId + '-download').href = pin['download_url'];
	document.getElementById(groupId + '-download').style.display = pin['download_url'] ? 'block' : 'none';
	document.getElementById(groupId + '-description').innerHTML = pin['description'];
			
	var worldMarker = document.getElementById(groupId + '-world-marker');
	worldMarker.style.left = pin['world_pos_x'] + 'px'; 
	worldMarker.style.top = pin['world_pos_y'] + 'px';
	
	var numVisiblePins = 0;
	for (var i = 0; i < pins.length; i++) {
		var pinVisible = (pins[i]['visible'] == 'true');
		var pagerImg = document.getElementById(groupId + '_pin' + i);
		if (pagerImg != null) {
			pagerImg.style.display = pinVisible ? 'inline-block' : 'none';
			pagerImg.src = layoutDir + 'pager_' + ((i == currIndex) ? 'current' : 'other') + '.png'; 
		}
		if (pinVisible) {
			numVisiblePins++;
		}
	}
	if (numVisiblePins <= 1) {
		for (var i = 0; i < pins.length; i++) {
			var pagerImg = document.getElementById(groupId + '_pin' + i);
			if (pagerImg != null) {
				pagerImg.style.display = 'none';
			}
		}
	}
}
