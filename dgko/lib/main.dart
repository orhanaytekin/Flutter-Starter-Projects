import 'package:confetti/confetti.dart';
import 'package:flutter/material.dart';
import 'package:assets_audio_player/assets_audio_player.dart';

void main() {
  AssetsAudioPlayer.setupNotificationsOpenAction((notification) {
    return true;
  });
  runApp(myApp());
}

// ignore: camel_case_types
class myApp extends StatelessWidget {
  const myApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
          //cardColor: const Color.fromRGBO(156, 39, 176, 1),
          //primaryColor: const Color.fromARGB(255, 1, 1, 1),
          //brightness: Brightness.light,
          //primaryColorDark: Colors.yellow,
          //primaryColorLight: Colors.black,
          ),
      debugShowCheckedModeBanner: false,
      home: MyApp(),
    );
  }
}

class MyApp extends StatefulWidget {
  final assetsAudioPlayer = AssetsAudioPlayer.newPlayer();
  MyApp({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _MyApp();
}

class _MyApp extends State<MyApp> {
  bool isPlaying2 = false;

  bool isPlaying = false;
  final controller = ConfettiController();
  // final String imgUrl = "assets/indir1.png";
  // AssetImage showImg = const AssetImage("assets/indir1.png");
  // final String imgUrl2 = "assets/indir2.png";
  // AssetImage showImg2 = const AssetImage("assets/indir2.png");
  // AssetImage showImg3 = const AssetImage("assets/indir2.png");

  /* void updateUI() {
    setState(() {
      showImg = AssetImage(imgUrl);
      Container(
      decoration: BoxDecoration(
        image: DecorationImage(
          fit: BoxFit.cover,
          image: showImg,
        ),
      ),
    );
    });
  }

  void updateUI2() {
    setState(() {
      showImg2 = AssetImage(imgUrl2);
      Container(
      decoration: BoxDecoration(
        image: DecorationImage(
          fit: BoxFit.cover,
          image: showImg2,
        ),
      ),
    );
    });
  } */

  @override
  void initState() {
    super.initState();
    // setAudio();
    widget.assetsAudioPlayer.open(
      Audio("assets/my_audio.mp3"),
      showNotification: true,
      autoStart: false,
    );
    controller.addListener(() {
      setState(() {
        isPlaying = controller.state == ConfettiControllerState.playing;
      });
    });
  }

  // Future setAudio() async {
  //   final player = AudioCache(prefix: "assets/",);
  //   final url = await player.load("my_audio.mp3");
  //   audioPlayer.setUrl(url.path,isLocal:true);
  // }

  @override
  void dispose() {
    controller.dispose();
    // audioPlayer.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Stack(alignment: Alignment.center, children: [
      Scaffold(
        backgroundColor: Colors.transparent,
        appBar: AppBar(
          title: const Center(child: Text("🎉Doğum Günün Kutlu Olsun🎉")),
        ),
        body: Stack(children: [
          Positioned.fill(
            child: Opacity(
              opacity: 0.75,
              child: Image.asset('assets/indir4.jpg', fit: BoxFit.cover),
            ),
          ),
          Center(
            child: MaterialButton(
              onPressed: () async {
                // PermissionStatus storage =
                //   await Permission.storage.request();
                // if(storage == PermissionStatus.granted) {
                if (isPlaying2) {
                  widget.assetsAudioPlayer.pause();
                } else {
                  widget.assetsAudioPlayer.play();
                  // }
                }
                setState(() {
                  isPlaying2 = !isPlaying2;
                });

                if (isPlaying) {
                  //updateUI2();
                  controller.stop();
                  // showImg3 = showImg2;

                } else {
                  //updateUI();
                  controller.play();
                  // showImg3 = showImg;
                }
              },
              child: Text(
                isPlaying ? "YETO" : "🥳🥳DGKO🥳🥳",
                style: const TextStyle(
                  color: Colors.blue,
                  fontSize: 20,
                ),
              ),
            ),
          ),
        ]),
      ),
      ConfettiWidget(
        confettiController: controller,
        shouldLoop: true,
        blastDirectionality: BlastDirectionality.explosive,
        emissionFrequency: 0.20,
        numberOfParticles: 15,
        gravity: 0.5,
        minBlastForce: 5,
        maxBlastForce: 50,
      ),
    ]);
  }
}
