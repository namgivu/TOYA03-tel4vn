--- official doc
fr google search ref https://docs.github.com/en/rest/repos/tags

fr error when try [bard answer](https://g.co/bard/share/9ba00d0aa766)
ref https://docs.github.com/rest/git/tags#create-a-tag-object
> {'message': 'Invalid request.\n\n"type" wasn\'t supplied.', 'documentation_url': 'https://docs.github.com/rest/git/tags#create-a-tag-object'}


--- create new tag
curl -L \
    -X POST \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer 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" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/repos/namgivu/TOYA03-tel4vn/git/tags \
    -d '{"tag":"v1","message":"create new tag","object":"57debfa8127e60b8386f8ee53752cb056109098f","type":"commit","tagger":{"name":"Nam G VU","email":"namgivu@gmail.com","date":"2023-09-26T11:22:33+07:00"}}'
