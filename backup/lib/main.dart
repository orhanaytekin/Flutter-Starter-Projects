import 'package:flutter/material.dart';
//import 'package:audioplayers/audioplayers.dart';
import 'package:just_audio/just_audio.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(

        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {

  MyHomePage({Key? key}) : super(key: key);

 
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> { 
  bool isPlaying = false;
  final player = AudioPlayer();
   @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: const Text("whatever"),
      ),
      body: SafeArea(
        child: Center(
          child: ElevatedButton(
            style:const ButtonStyle(
              
            ),
            child: Icon(
              isPlaying ? Icons.pause : Icons.play_arrow,
  ),
            onPressed: (){

              if(!isPlaying) {
              player.setUrl("indir11.mp3");
              player.play();
              isPlaying = true;}
              else{
                player.stop();
                isPlaying = false;
              }
              
            },
          ),
        ),
        ),
    );
  }
}



  

 