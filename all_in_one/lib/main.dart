import 'dart:io';
import 'globals.dart';
import 'package:all_in_one/surprise.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:image_picker/image_picker.dart';
import 'package:permission_handler/permission_handler.dart';
import 'list_photos.dart';
import 'liquidview.dart';
import 'my_alert_dialog.dart';
import 'user.dart';
import 'package:assets_audio_player/assets_audio_player.dart';
import 'package:confetti/confetti.dart';
import 'package:flutter_svg/svg.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'COMPILATION Demo',
      theme: ThemeData.dark(),
      initialRoute: '/',
      routes: {
        '/': (context) => MyHomePage(),
        '/LP': (context) => const ListPhotos(),
        '/LV': (context) => LiquidView(),
        '/User': (context) => User(),
        '/S': (context) => const Surprise(),
      },
      debugShowCheckedModeBanner: false,
    );
  }
}

// ignore: must_be_immutable
class MyHomePage extends StatefulWidget {
  static List<XFile>? imageFileList = [];
  File? file = User.file;
  String? filePath = User.filePath;
  MyHomePage({Key? key}) : super(key: key);

  @override
  State<MyHomePage> createState() => MyHomePageState();
}

class MyHomePageState extends State<MyHomePage> {
  // ImagePicker image = ImagePicker();
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();
  final controller = ConfettiController(duration: const Duration(seconds: 3));
  static final audioSpongeBob = AssetsAudioPlayer();
  static final audioDarkSpongeBob = AssetsAudioPlayer();

  File? profileFile = User.file;
  final ImagePicker _picker = ImagePicker();
  List<Widget>? keep_these = [];
  List<Widget> warHero = [];
  // bool _selected = false;
  static bool isPlaying = false;
  static bool isDarkPlaying = false;
  bool isConfettiPlaying = false;
  callback() {
    setState(() {});
  }

  @override
  void initState() {
    controller.addListener(() {
      setState(() {
        isConfettiPlaying = controller.state == ConfettiControllerState.playing;
      });
    });

    super.initState();
    audioSpongeBob.open(
      Audio("assets/audios/spongebobreal.mp3"),
      headPhoneStrategy: HeadPhoneStrategy.pauseOnUnplug,
      respectSilentMode: false,
      showNotification: false,
      autoStart: false,
    );

    audioSpongeBob.playlistAudioFinished.listen((Playing playing) {
      setState(() {
        isPlaying = false;
      });
    });
    audioDarkSpongeBob.open(
      Audio("assets/audios/cursed.mp3"),
      headPhoneStrategy: HeadPhoneStrategy.pauseOnUnplug,
      loopMode: LoopMode.playlist,
      respectSilentMode: false,
      showNotification: false,
      autoStart: false,
    );

    audioDarkSpongeBob.playlistAudioFinished.listen((Playing playing) {
      setState(() {
        isDarkPlaying = false;
      });
    });
  }

  @override
  void dispose() {
    super.dispose();
    controller.dispose();
    audioSpongeBob.dispose();
    audioDarkSpongeBob.dispose();
    isPlaying = isDarkPlaying = false;
  }

  Future<bool> _onWillPop() async {
    if (_scaffoldKey.currentState!.isDrawerOpen ||
        _scaffoldKey.currentState!.isEndDrawerOpen) return true;
    return (await showDialog(
          context: context,
          builder: (context) => AlertDialog(
            title: const Text('Are you sure?'),
            content: const Text('Do you want to exit?'),
            actions: <Widget>[
              TextButton(
                onPressed: () =>
                    Navigator.of(context).pop(false), //<-- SEE HERE
                child: const Text('No'),
              ),
              TextButton(
                onPressed: () =>
                    Navigator.of(context).pop(true), // <-- SEE HERE
                child: const Text('Yes'),
              ),
            ],
          ),
        )) ??
        false;
  }

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: _onWillPop,
      child: Scaffold(
        key: _scaffoldKey,
        drawer: Drawer(
          backgroundColor: Globals.selected == false
              ? const Color.fromARGB(255, 85, 76, 0)
              : Colors.black,
          child: ListView(
            // Important: Remove any padding from the ListView.
            padding: EdgeInsets.zero,
            children: [
              DrawerHeader(
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: Globals.selected == false
                        ? const AssetImage("assets/gifs/spongebob.gif")
                        : const AssetImage("assets/gifs/drawer.gif"),
                    fit: BoxFit.cover,
                  ),
                  color: Globals.selected == false ? Colors.blue : Colors.red,
                ),
                child: null,
              ),
              ListTile(
                leading: const Icon(
                  Icons.home,
                ),
                title: const Text('Home Page'),
                onTap: () {
                  Navigator.pop(context);
                },
              ),
              ListTile(
                leading: const Icon(
                  Icons.list,
                ),
                title: const Text('List'),
                onTap: () {
                  Navigator.pushNamed(context, '/LP');
                  setState(() {});
                },
              ),
              ListTile(
                leading: const Icon(
                  Icons.slideshow,
                ),
                title: const Text('Slide'),
                onTap: () {
                  Navigator.pushNamed(context, '/LV');
                  setState(() {});
                },
              ),
              // const SizedBox(height: 8),
              const Divider(color: Colors.white70),
              // const SizedBox(height: 8),
              const AboutListTile(
                // <-- SEE HERE
                icon: Icon(
                  Icons.info,
                ),
                applicationIcon: Icon(
                  Icons.local_play,
                ),
                applicationName: 'Orhan',
                applicationVersion: '28.09.2002',
                applicationLegalese: '© 2022 Company',
                aboutBoxChildren: [
                  ///Content goes here...
                ],
                child: Text('About app'),
              ),
            ],
          ),
        ),
        backgroundColor: Globals.selected == false
            ? const Color.fromARGB(200, 229, 228, 114)
            : Colors.black,
        bottomNavigationBar: BottomAppBar(
          color: Globals.selected == false
              ? const Color.fromARGB(200, 229, 228, 114)
              : Colors.black,
          child: Row(
            children: [
              const SizedBox(width: 16),
              Container(
                height: 40,
                width: 110,
                alignment: Alignment.bottomLeft,
                child: FittedBox(
                  child: ChoiceChip(
                    clipBehavior: Clip.hardEdge,
                    label: Globals.selected == true
                        ? const Icon(Icons.dark_mode)
                        : const Icon(Icons.light_mode),
                    selected: Globals.selected,
                    onSelected: (bool newValue) {
                      if (Globals.selected == false) {
                        showDialog<String>(
                          barrierDismissible: true,
                          context: context,
                          builder: (BuildContext context) => AlertDialog(
                            title: const Text('Activate Dark Mode',
                                style: TextStyle(color: Colors.redAccent)),
                            content: const Text(
                                'You are about to activate the dark mode, use it carefully, you don\'t know what you are up against.\n(PS: CONFETTI DOESN\'T WORK WHEN THE DARK MODE IS ON, YOU WON\'T NEED IT ANYWAYS.)'),
                            actions: <Widget>[
                              Row(
                                children: [
                                  const Icon(Icons.dark_mode),
                                  TextButton(
                                    onPressed: () {
                                      Navigator.pop(context, 'Cancel');
                                      setState(() {
                                        User.filePath =
                                            "assets/dark_mode/default.jpg";
                                        audioSpongeBob.dispose();
                                        audioDarkSpongeBob.dispose();
                                        UserState.audioOzge.dispose();
                                        UserState.audioDarkOzge.dispose();
                                        isPlaying = isDarkPlaying = false;
                                        UserState.isPlaying =
                                            UserState.isDarkPlaying = false;
                                        Globals.selected = newValue;
                                      });
                                    },
                                    child: const Text('ACTIVATE'),
                                  ),
                                  const Spacer(),
                                  const Icon(Icons.light_mode),
                                  TextButton(
                                    onPressed: () {
                                      Navigator.pop(context, 'Continue');
                                    },
                                    child: const Text('STAY'),
                                  ),
                                ],
                              ),
                            ],
                          ),
                        );
                      } else {
                        // Navigator.pop(context);
                        setState(() {
                          User.filePath = "assets/light_mode/shiro.jpg";
                          audioSpongeBob.dispose();
                          audioDarkSpongeBob.dispose();
                          UserState.audioOzge.dispose();
                          UserState.audioDarkOzge.dispose();
                          isPlaying = isDarkPlaying = false;
                          UserState.isPlaying = UserState.isDarkPlaying = false;
                          Globals.selected = newValue;
                        });
                      }
                    },
                  ),
                ),
              ),
              const Spacer(),
              Stack(
                children: [
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
                  IconButton(
                    icon: Globals.selected == false
                        ? (isConfettiPlaying == false
                            ? const Icon(
                                Icons.celebration,
                                color: Colors.black,
                              )
                            : const Icon(
                                Icons.stop,
                                color: Colors.red,
                              ))
                        : const Icon(
                            Icons.celebration,
                            color: Colors.red,
                          ),
                    onPressed: () {
                      if (Globals.selected == false) {
                        if (isConfettiPlaying) {
                          controller.stop();
                        } else {
                          controller.play();
                        }
                      } else {
                        null;
                      }
                    },
                  ),
                ],
              ),
              const SizedBox(width: 16),
            ],
          ),
        ),
        floatingActionButton: MyAlertDialog(),
        floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
        //ackgroundColor: Colors.yellow,
        appBar: AppBar(
          leading: Builder(
            builder: (BuildContext context) {
              return IconButton(
                icon: Icon(
                  Icons.menu,
                  color: Globals.selected == false ? Colors.black : Colors.red,
                  // size: 44, // Changing Drawer Icon Size
                ),
                onPressed: () {
                  Scaffold.of(context).openDrawer();
                },
                tooltip: MaterialLocalizations.of(context).openAppDrawerTooltip,
              );
            },
          ),
          backgroundColor: Globals.selected == false
              ? const Color.fromARGB(200, 229, 228, 114)
              : Colors.black,
          title: Center(
            child: FittedBox(
                child: Text(
              "SpongeBob SquarePants",
              style: TextStyle(
                color: Globals.selected == false ? Colors.black : Colors.red,
              ),
            )),
          ),
          actions: [
            Builder(
              builder: (BuildContext context) {
                return IconButton(
                  icon: Icon(
                    Icons.account_circle_sharp,
                    color:
                        Globals.selected == false ? Colors.black : Colors.red,
                    // size: 44, // Changing Drawer Icon Size
                  ),
                  onPressed: () {
                    Scaffold.of(context).openEndDrawer();
                    if (Scaffold.of(context).isEndDrawerOpen == true) {
                      setState(() {});
                    }
                  },
                  tooltip:
                      MaterialLocalizations.of(context).openAppDrawerTooltip,
                );
              },
            ),
          ],
          //backgroundColor: Colors.yellow,
        ),

        body: Column(
          children: [
            IconButton(
              onPressed: () {
                if (Globals.selected == false) {
                  audioSpongeBob.playOrPause();

                  if (!audioSpongeBob.isPlaying.value) {
                    setState(() {
                      //audioSpongeBob.dispose();
                      isPlaying = false;
                    });
                  }

                  setState(() {
                    isPlaying = !isPlaying;
                  });
                } else {
                  audioDarkSpongeBob.playOrPause();

                  if (!audioDarkSpongeBob.isPlaying.value) {
                    setState(() {
                      // audioDarkSpongeBob.dispose();
                      isDarkPlaying = false;
                    });
                  }

                  setState(() {
                    isDarkPlaying = !isDarkPlaying;
                  });
                }
              },
              icon: Globals.selected == false
                  ? (isPlaying == true
                      ? const Icon(
                          Icons.pause,
                          color: Colors.red,
                        )
                      : const Icon(
                          Icons.audiotrack,
                          color: Colors.greenAccent,
                        ))
                  : (isDarkPlaying == true
                      ? const Icon(
                          Icons.radio_button_checked,
                          color: Colors.blueAccent,
                        )
                      : const Icon(
                          Icons.dangerous,
                          color: Colors.red,
                        )),
            ),
            SizedBox(
                height: MediaQuery.of(context).size.height * 0.5,
                width: double.infinity,
                child: Globals.selected == false
                    ? Image.asset(
                        "assets/light_mode/spongebob.jpg",
                        fit: BoxFit.cover,
                      )
                    : Image.asset(
                        "assets/dark_mode/indir3.png",
                        fit: BoxFit.cover,
                      )),
            // Container(
            //   height: 400,
            // ),
            // ElevatedButton(
            //     style: ButtonStyle(
            //       backgroundColor: MaterialStateColor.resolveWith(
            //         (states) => Colors.green.shade500,
            //       ),
            //     ),
            //     onPressed: () async {
            //       int count = await selectImages();

            //       // ignore: use_build_context_synchronously
            //       ScaffoldMessenger.of(context).removeCurrentSnackBar();
            //       // ignore: use_build_context_synchronously
            //       ScaffoldMessenger.of(context).showSnackBar(
            //         SnackBar(
            //           duration: const Duration(seconds: 2),
            //           elevation: 0,
            //           behavior: SnackBarBehavior.floating,
            //           content: Text("You have selected $count images total."),
            //         ),
            //       );
            //       setState(() {});
            //       print("$count images total");
            //     },
            //     child: const Text("Add Image(s)")),
            // ElevatedButton(
            //     style: ButtonStyle(
            //       backgroundColor: MaterialStateColor.resolveWith(
            //         (states) => Colors.blueGrey.shade200,
            //       ),
            //     ),
            //     onPressed: () {
            //       Navigator.pushNamed(context, '/LP');
            //       setState(() {});
            //     },
            //     child: const Text("List Image(s)")),
            // ElevatedButton(
            //     style: ButtonStyle(
            //       backgroundColor:
            //           MaterialStateColor.resolveWith((states) => Colors.blue),
            //     ),
            //     onPressed: () {
            //       Navigator.pushNamed(context, '/LV');
            //       setState(() {});
            //     },
            //     child: const Text("Go To Swipe Page")),
            const SizedBox(height: 16),
            Center(
              //TODO CHANGE THE TEXTS ACCORDING TO DARK AND LIGHT MODE
              child: Globals.selected == false
                  ? const Text(
                      "Welcome! Don't forget to click EVERYTHING.",
                      style: TextStyle(
                        color: Colors.black,
                        fontSize: 16,
                      ),
                    )
                  : const Text(
                      "GET OUT!",
                      style: TextStyle(
                        color: Colors.red,
                      ),
                    ),
            ),
            const SizedBox(height: 16),

            ElevatedButton(
                style: ButtonStyle(
                  backgroundColor:
                      MaterialStateColor.resolveWith((states) => Colors.red),
                ),
                onPressed: () {
                  showDialog<String>(
                    barrierDismissible: true,
                    context: context,
                    builder: (BuildContext context) => AlertDialog(
                      title: const Text('Reset',
                          style: TextStyle(color: Colors.redAccent)),
                      content: const Text(
                          'You are about to reset the program, if you continue you will have to add image(s) again.'),
                      actions: <Widget>[
                        Row(
                          children: [
                            const Icon(Icons.restart_alt_sharp),
                            TextButton(
                              onPressed: () {
                                MyHomePage.imageFileList!.clear();
                                keep_these!.clear();
                                Globals.selected = false;
                                audioSpongeBob.dispose();
                                UserState.audioOzge.dispose();
                                audioDarkSpongeBob.dispose();
                                UserState.audioDarkOzge.dispose();
                                isPlaying = isDarkPlaying = false;
                                UserState.isPlaying =
                                    UserState.isDarkPlaying = false;
                                User.filePath = "assets/light_mode/shiro.jpg";
                                // ListPhotosState.widgets.clear();
                                // LiquidViewState.widgets.clear();
                                Navigator.pop(context, 'Cancel');
                                setState(() {});
                              },
                              child: const Text('Reset'),
                            ),
                            const Spacer(),
                            const Icon(Icons.cancel),
                            TextButton(
                              onPressed: () {
                                Navigator.pop(context, 'Continue');
                              },
                              child: const Text('Cancel'),
                            ),
                          ],
                        ),
                      ],
                    ),
                  );
                  // setState(() {});
                },
                child: const Text("Reset")),
          ],
        ),
        endDrawer: Drawer(
          backgroundColor: Globals.selected == false ? null : Colors.black,
          width: MediaQuery.of(context).size.width * 0.6,
          child: ListView(
            // Important: Remove any padding from the ListView.
            padding: EdgeInsets.zero,
            children: [
              UserAccountsDrawerHeader(
                onDetailsPressed: () {
                  Navigator.pushNamed(context, "/User");
                  MyHomePageState.audioDarkSpongeBob.dispose();
                  MyHomePageState.isDarkPlaying = false;
                  MyHomePageState.audioSpongeBob.dispose();
                  MyHomePageState.isPlaying = false;
                  setState(() {});
                },
                // <-- SEE HERE
                // arrowColor: Colors.green,
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: Globals.selected == false
                        ? const AssetImage("assets/light_mode/indir.jpg")
                        : const AssetImage("assets/dark_mode/enddrawer.jpg"),
                    fit: BoxFit.cover,
                    opacity: 9,
                  ),
                ),
                accountName: const Text(
                  "",
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: Colors.black,
                    fontSize: 16,
                    // color: Color.fromARGB(255, 169, 151, 151),
                  ),
                ),
                accountEmail: const Text(
                  "Özge ERDEM",
                  style: TextStyle(
                    fontWeight: FontWeight.w900,
                    color: Colors.white,
                  ),
                ),
                currentAccountPicture: CircleAvatar(
                  child: ClipOval(
                    child: User.filePath == ''
                        ? Image.file(
                            User.file!,
                            fit: BoxFit.cover,
                            height: MediaQuery.of(context).size.width * 0.2,
                            width: MediaQuery.of(context).size.width * 0.2,
                          )
                        : Image.asset(
                            User.filePath!,
                            fit: BoxFit.cover,
                            height: MediaQuery.of(context).size.width * 0.2,
                            width: MediaQuery.of(context).size.width * 0.2,
                          ),
                  ),
                ),
              ),
              ListTile(
                leading: const Icon(Icons.person),
                title: const Text('Profile'),
                onTap: () {
                  Navigator.pushNamed(context, '/User');
                  MyHomePageState.audioDarkSpongeBob.dispose();
                  MyHomePageState.isDarkPlaying = false;
                  MyHomePageState.audioSpongeBob.dispose();
                  MyHomePageState.isPlaying = false;

                  setState(() {});
                },
              ),
              ListTile(
                leading: Globals.selected == false
                    ? const Icon(
                        Icons.wallet_giftcard,
                      )
                    : const Icon(Icons.bug_report, color: Colors.purple),
                title: Globals.selected == false
                    ? const Text('Bonus')
                    : const Text('PLANKTON',
                        style: TextStyle(color: Colors.purple)),
                onTap: () {
                  Navigator.pushNamed(context, '/S');
                },
              ),
              const Divider(),
              ListTile(
                leading: const Icon(
                  Icons.exit_to_app,
                  color: Colors.red,
                ),
                title: const Text(
                  'Quit',
                  style: TextStyle(color: Colors.red),
                ),
                onTap: () {
                  showDialog<String>(
                    barrierDismissible: true,
                    context: context,
                    builder: (BuildContext context) => AlertDialog(
                      title: const Text('You are about to quit!',
                          style: TextStyle(color: Colors.redAccent)),
                      content: const Text(
                          'All of the added images and profile picture\'s data will be lost.'),
                      actions: <Widget>[
                        Row(
                          children: [
                            const Icon(Icons.exit_to_app, color: Colors.red),
                            TextButton(
                              onPressed: () {
                                Navigator.pop(context, 'Continue');
                                SystemNavigator.pop();
                              },
                              child: const Text('Quit',
                                  style: TextStyle(color: Colors.red)),
                            ),
                            const Spacer(),
                            const Icon(Icons.cancel, color: Colors.green),
                            TextButton(
                              onPressed: () {
                                Navigator.pop(context, 'Cancel');
                              },
                              child: const Text('Cancel',
                                  style: TextStyle(color: Colors.green)),
                            ),
                          ],
                        ),
                      ],
                    ),
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future<int> selectImages() async {
    final List<XFile>? selectedImages = await _picker.pickMultiImage();
    if (selectedImages!.isNotEmpty) {
      MyHomePage.imageFileList!.addAll(selectedImages);
    }
    return MyHomePage.imageFileList!.length;
  }

//TODO FOR LOOP INSTEAD  ---> REMOVE DUPLICATES
  void showImagesBuilder() {
    GridView.builder(
      itemCount: MyHomePage.imageFileList!.length,
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
      ),
      itemBuilder: (BuildContext context, int index) {
        File file = File(MyHomePage.imageFileList![index].path);
        return showImages("file", "", file);
      },
    );
  }

  Widget showImages(
    String type,
    String filePath,
    File file,
  ) {
    return Container(
      color: Colors.red,
      padding: const EdgeInsets.all(24),
      child: ListView(
        children: [
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              type == "asset"
                  ? Image.asset(
                      filePath,
                      fit: BoxFit.cover,
                      width: double.infinity,
                    )
                  : Image.file(
                      file,
                      fit: BoxFit.fitHeight,
                      width: double.infinity,
                    ),
              const SizedBox(height: 64),
              const Text(
                "title",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 46,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 24),
              Container(
                padding: const EdgeInsets.only(right: 32),
                // child: const TextField(
                //     obscureText: true,
                //     decoration: InputDecoration(
                //       border: OutlineInputBorder(),
                //       labelText: 'Password',
                //     )),
                child: const Text(
                  "subtitle",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 20,
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  // getcam() async {
  //   // ignore: deprecated_member_use
  //   var img = await image.getImage(source: ImageSource.camera);
  //   setState(() {
  //     imageFileList!.add(img as XFile);
  //   });
  // }
}
