var packName = pack.getPackName(); // Get the script's pack name. In this case it will be : example_pack

console.log("Hello from the official gameplay script: " + packName); // Print a message when the script is loaded (This means when the content-pack is loaded/reloaded)

/* Events */
ItemEvents.dropped("minecraft:cobblestone", event => { // On cobble is dropped, print a message in the console and cancel the drop. (The item will still be in the user inventory)
	console.log("Blocked a cobblestone drop in pack " + packName); // The message contains the global variable "packName"
	e.cancel();
});

ItemEvents.dropped("m4a4", event => {
	console.log("Custom Item dropped: " + event.getItemId()); // Print a message when the item is dropped. The message will contain the item ID (minecraft:stick, niwer_engine:m4a4, etc)
});

ItemEvents.interact("minecraft:stick", event => { // When interacting on an entity with a stick, print a message in the console
	console.log("Stick interacted !");
});