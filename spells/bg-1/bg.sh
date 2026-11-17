#!/bin/sh

URL[0]='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/528e6562-a8bf-4e04-ac77-a7f72fed2987/dftjfsn-dbebf1d3-03b8-4652-a964-a395d554ce22.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzUyOGU2NTYyLWE4YmYtNGUwNC1hYzc3LWE3ZjcyZmVkMjk4N1wvZGZ0amZzbi1kYmViZjFkMy0wM2I4LTQ2NTItYTk2NC1hMzk1ZDU1NGNlMjIuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.jwAuCwU-tzDecl9gLI0W5fpmJsg25JL0fChmn6YHLwE'


chosen_url=$[$RANDOM % ${#URL[@]}]

feh --bg-scale $URL

if [ -d ~/afs ] ; then
  echo "exec --no-startup-id feh --bg-scale $URL " >> ~/afs/.confs/i3/config
fi
