import groovy.json.JsonSlurper
import groovy.json.JsonOutput


def jsonSlurper = new JsonSlurper()
def movie = jsonSlurper.parseText(new String(payload))


def connection = new URL( "https://imdb8.p.rapidapi.com/title/get-details?tconst=${movie.imdb}")
                 .openConnection() as HttpURLConnection

connection.setRequestProperty( 'x-rapidapi-host', 'imdb8.p.rapidapi.com' )
connection.setRequestProperty( 'x-rapidapi-key', '2ee82876a6msh3fc242639f601a0p13b445jsncf1ac4d987c0')
connection.setRequestProperty( 'Accept', 'application/json' )
connection.setRequestProperty( 'Content-Type', 'application/json')

if ( connection.responseCode == 200 ) {
    
    def imdb = connection.inputStream.withCloseable { inStream ->
        new JsonSlurper().parse( inStream as InputStream )
    }
    
    movie.imdb = [ "image": imdb.image.url ]   

} else {
    println connection.responseCode + ": " + connection.inputStream.text
}

JsonOutput.toJson(movie)
