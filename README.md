# Emotional-Support-Discord-Bot
Light hearted personal project for use in a discord group of close friends

Command-based bot that only has read/write permissions.

Responds to the following commands:

	• !help: Display a list of all available commands.

	• !greeting: Greet a user with a random greeting.

	• !happy: Sends words of encouragement.

	• !dragon: Post a random picture of a dragon.

	• /vent: Send a private vent message to the bot, and it will send private words of encouragement back.

Instructions for personal use:

	• Create a new bot application in the discord developer panel: https://discord.com/developers/applications
	
	• Copy the token of your bot and paste it in quotations in the provided .env file

	• In the OAuth2 tab, generate a URL with the following values:

	    ° Scopes: Bot
	
	    ° Permissions:
	
	        • General: Read messages/view channels
		
	        • Text: ALL PERMISSIONS EXCEPT; Send TTS, Use embedded activities
