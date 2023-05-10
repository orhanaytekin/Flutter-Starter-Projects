import 'package:flutter/material.dart';
import 'package:audioplayers/audioplayers.dart';

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
      debugShowCheckedModeBanner: false,
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
  void initState() {
    player.onPlayerStateChanged.listen(
      (state) {
        setState(
          () {
            player.onPlayerStateChanged.listen(
              (state) {
                isPlaying = state == PlayerState.playing;
              },
            );
          },
        );
      },
    );

    super.initState();
  }

  @override
  void dispose() {
    player.dispose();
    // audioPlayer.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: const Center(child: Text("ALLAH DİYEN UYGULAMA")),
      ),
      body: Center(
        child: MaterialButton(
          onPressed: () {
            if (isPlaying) {
              player.stop();
            } else {
              player.play(UrlSource("assets/indir12.mp3"));
            }
            //isPlaying = !isPlaying;
          },
          //Icon(isPlaying ? Icons.pause : Icons.play_arrow),
          child: //Icon(isPlaying ? Icons.pause : Icons.play_arrow),
              Text(isPlaying ? "DUR" : "ZİKRET"),
        ),
      ),
    );
  }
}
