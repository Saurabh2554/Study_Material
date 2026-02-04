# 1. WHat is authentication? 
 ANS: The process of verifying whether a user exist in the database or not by checking their username/email and password is called Authentication. 
      There are various ways in which this process and be implemented: 
        1. Session Based Authentication
        2. Token Based Authentication(JWT)
        3. OAuth 

# 2. What is the process involved in the authentication? Or how does authentication takes place?
 ANS: When a user tries to login providing their username and password. The server tries to validate first whether user with the given username/email already exist in the database or not, if yes then it tries to compare the password with what stored in the DB. The password verification phase involve decrypting password from both the side. Once it is verified, server tries to generate a session containing {session-key: session-value} by using user creds(payload) and expiration-time and then send this session to the client for further request. This process typically happend when we choose session based auth. The server also stores this session in it's own cache/db too. 
 But if we choose JWT based auth, the process is little bit different. After verification Auth server generates two tokens named access-token and refresh token. Access token are generally short lived and refresh-roken are long lived. In case if access token expires it can be regenerated using the refresh token, but if refresh token expires, user will have to login again.         

# 3. Difference between Session based and Token based Authentication.
 ANS: __Session vs. Token-Based Authentication__
        Maintaining authentication (without hassling users) across a stateless HTTP connection is an important problem because no one wants to enter their password every time they make a request.

        ___{Session-based authentication}___ (an older method) relies on the server to track authentication. When a user logs in to a website on a browser, the server creates a session for that user. A session ID is assigned and stored in a cookie in the user's browser, preserving authentication while the user is on the site. Typically, cookies are deleted when a user logs off, but some browsers use session restoring, which keeps the session cookies in memory even after the user logs off. Much easier than logging in each time you want to access a page.

        ___{Token-based authentication}___is different. When a user logs in, the server creates an encrypted token that allows users to perform any activity on the site. Instead of the server storing session IDs, the client stores the token, either in memory or in a cookie (much like session IDs.)

        The main difference between token and traditional session-based authentication is that session-based authentication is very stateful. The server stores the session ID and user info in memory or in a separate session cache, which can become complex as the system or number of users scale.

        Token-based authentication is not always stateless, though. Many API tokens are still stored in a database table so they can be verified or revoked.  

# 4. Where do we store each token in token based authentication(JWT)?
 ANS: JWT Authentication method claim to be stateless as it need not to be stored on server side where as on cliend side we can store it in local storage, cookie, or in memory. 
 Since access token are short-lived and need not to be stored on server side, whereas there are multiple theories regarding storage of Refresh-token on server side. 
 1. We can store the refresh token per user in a Database or in cache but as the complexity grows(when not of server and DB grows) it can be a bottleneck.
 2. We can use a concept called  __{Refresh Token Rotation}__, which states that whenever access token expires and client request for new access token, also generates the   new refresh token and share to the client keeping the server save. But here arise a question, What's the point of long lived refresh token?
 3. We can use another concept called __{Refresh Token Automatic Reuse Detection}__ which states that, it is impossible to guess which user is malicious or which is legitimate only based on a token, as malicious can steal the token and can act as legitimate one. so the best approach is treat each every user as malicious and generate Token family per user. For more reading ref: https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/#Refresh-Token-Automatic-Reuse-Detection

