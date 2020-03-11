Permission system - one dict per room {username} -> [string], where each user would have a list of permissions
the server would check if given action is in the list

could contain things like use files (or more detailed), whisper, change persona etc
most likely will require additional model with serialization to string (or json)






work plan:
set up endpoints with proper auth <--
add database integration (including file handling)
set up websockets