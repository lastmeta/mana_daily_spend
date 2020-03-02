package com.simplesurplus.simplesurplus

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    // when app runs...
    // does json file exist? is it valid?
    // no: start tutorial which will save json file
    // yes: show main screen

    // upon tutorial load...
    // ask: how much do you make each month?
    // ask: how much do you spend on bills each month?
    // ask: how much do you want to save each month?
    // derive daily limit amount: (total - bills - savings) / 30
    // save all daily limit to json file
    // tell user their daily limit
    // tell user that this app will keep track of their daily limit surplus or debt.
    // load main screen

    // upon main screen load...
    // get json file data:
    // daily limit, surplus amount, last day surplus was calculated.
    // calculate and save surplus amount. Save today as the last day it was calculated.
    // display daily limit, surplus amount and area for a new transaction input (number textbox)
    // display daily limit and surplus amount in number textboxes as well, if they change the numbers for these update the json file.
    // if they add a new transaction minus transaction amount from surplus. save surplus to json file. and last transaction amount.

    // lastly make a notification that occurs once a day asking them how much they spent that day.
    // allow them to answer in the notification itself instead of opening the app if possible.
    // either way show them their surplus after they have answered the question.

    // page nav
    //helloworld.OnClickListener {
    //    startActivity(Intent(this, AboutMe::class.java)
    //}

    //private fun writeJSONtoFile(s:String) {
    //    //Create list to store the all Tags
    //    var tags = ArrayList<String>()
    //    // Add the Tag to List
    //    tags.add("Android")
    //    tags.add("Angular")
    //    //Create a Object of Post
    //    var post = Post("Json Tutorial", "www.nplix.com", "Pawan Kumar", tags)
    //    //Create a Object of Gson
    //    var gson = Gson()
    //    //Convert the Json object to JsonString
    //    var jsonString:String = gson.toJson(post)
    //    //Initialize the File Writer and write into file
    //    val file=File(s)
    //    file.writeText(jsonString)
    //}

    //private fun readJSONfromFile(f:String) {
    //
    //    //Creating a new Gson object to read data
    //    var gson = Gson()
    //    //Read the PostJSON.json file
    //    val bufferedReader: BufferedReader = File(f).bufferedReader()
    //    // Read the text from buffferReader and store in String variable
    //    val inputString = bufferedReader.use { it.readText() }
    //
    //    //Convert the Json File to Gson Object
    //    var post = gson.fromJson(inputString, Post::class.java)
    //    //Initialize the String Builder
    //    stringBuilder = StringBuilder("Post Details\n---------------------")
    //    +Log.d("Kotlin",post.postHeading)
    //    stringBuilder?.append("\nPost Heading: " + post.postHeading)
    //    stringBuilder?.append("\nPost URL: " + post.postUrl)
    //    stringBuilder?.append("\nPost Author: " + post.postAuthor)
    //    stringBuilder?.append("\nTags:")
    //    //get the all Tags
    //
    //    post.postTag?.forEach { tag -> stringBuilder?.append(tag + ",") }
    //    //Display the all Json object in text View
    //    textView?.setText(stringBuilder.toString())
    //
    //}
}
