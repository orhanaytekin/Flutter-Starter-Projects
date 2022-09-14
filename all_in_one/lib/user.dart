// ignore_for_file: use_build_context_synchronously

import 'dart:convert';
import 'dart:io';
import 'dart:math';
import 'dart:typed_data';
import 'globals.dart';
import 'package:assets_audio_player/assets_audio_player.dart';
import 'package:confetti/confetti.dart';
import 'package:flutter/services.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'main.dart';
import "package:gallery_saver/gallery_saver.dart";
import 'back_button_handler.dart';
import 'package:path_provider/path_provider.dart';
import 'package:dio/dio.dart';
import 'package:image_gallery_saver/image_gallery_saver.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:shared_preferences/shared_preferences.dart';

// class User extends StatelessWidget {
//   String? filePath = "assets/indir.jpg";
//   ImagePicker image = ImagePicker();

//   User({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       debugShowCheckedModeBanner: false,
//       theme: ThemeData(
//         scaffoldBackgroundColor: Colors.greenAccent,
//         appBarTheme: const AppBarTheme(
//           color: Colors.greenAccent,
//         ),
//       ),
//       home: Scaffold(
//         appBar: AppBar(
//           leading: IconButton(
//             onPressed: () {
//               Navigator.pop(context);
//             },
//             color: Colors.black,
//             icon: const Icon(Icons.arrow_back),
//           ),
//           title: const FittedBox(
//             child: Text(
//               "Profile",
//               style: TextStyle(
//                 color: Colors.black,
//               ),
//             ),
//           ),
//         ),
//         body: Center(
//           child: Column(
//             children: [
//               const SizedBox(height: 16),
//               const Center(
//                 child: Text(
//                   'ÖZGE ERDEM',
//                   style: TextStyle(
//                     color: Colors.purpleAccent,
//                     fontWeight: FontWeight.bold,
//                     fontSize: 16,
//                   ),
//                 ),
//               ),
//               const SizedBox(height: 16),
//               CircleAvatar(
//                 backgroundImage: AssetImage(filePath!),
//                 radius: 150,
//               ),
//               const SizedBox(height: 20),
//               const Center(
//                 child: Text(
//                   'Doğum günün kutlu olsun yoldaş!',
//                   style: TextStyle(
//                     color: Colors.red,
//                     fontWeight: FontWeight.bold,
//                     fontSize: 16,
//                   ),
//                 ),
//               ),
//               const Divider(),
//               MaterialButton(
//                 child: const Text("Click"),
//                 onPressed: () {
//                   showDialog(
//                     context: context,
//                     builder: (BuildContext context) {
//                       return AlertDialog(
//                         title: Center(
//                           child: Image.asset("assets/spongebob.gif",
//                               fit: BoxFit.fill),
//                         ),
//                         // content:
//                         //     const Center(child: Text("Nice mutlu yıllara...")),
//                         actions: const [
//                           // TextButton(
//                           //   onPressed: () {},
//                           //   child: Image.asset("assets/spongebob.gif",
//                           //       fit: BoxFit.cover),
//                           // )
//                         ],
//                       );
//                     },
//                   );
//                 },
//               ),
//               const Divider(),
//               MaterialButton(
//                 onPressed: () {
//                   showDialog(
//                     context: context,
//                     builder: (BuildContext context) {
//                       return AlertDialog(
//                         title: const Text("Please choose one"),
//                         content: const Text(
//                             "Pick an image from gallery or take one from camera."),
//                         // content:
//                         //     const Center(child: Text("Nice mutlu yıllara...")),
//                         actions: <Widget>[
//                           Row(
//                             children: [
//                               const Icon(Icons.camera_alt),
//                               TextButton(
//                                 onPressed: () async {
//                                   XFile? img = await image.pickImage(
//                                       source: ImageSource.camera);
//                                   filePath = img!.path;
//                                 },
//                                 child: const Text('Camera'),
//                               ),
//                               const Spacer(),
//                               const Icon(Icons.photo),
//                               TextButton(
//                                 onPressed: () async {
//                                   XFile? img = await image.pickImage(
//                                       source: ImageSource.gallery);
//                                   filePath = img!.path;
//                                 },
//                                 child: const Text('Gallery'),
//                               ),
//                             ],
//                           ),
//                         ],
//                       );
//                     },
//                   );
//                 },
//                 child: const Text("Change profile picture"),
//               ),
//               const Divider(),
//               TextButton(
//                 onPressed: () {},
//                 child: const Text("Bonus"),
//               )
//             ],
//           ),
//         ),
//       ),
//     );
//   }
// }

class User extends StatefulWidget {
  static String? filePath = Globals.selected == false
      ? "assets/light_mode/shiro.jpg"
      : "assets/dark_mode/default.jpg";
  static File? file;
  List<Widget> widgets = [];
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();
  // Function callbackFunction;
  User({Key? key}) : super(key: key);

  @override
  State<User> createState() => UserState();
}

class UserState extends State<User> {
  Color colorOfDivider =
      Globals.selected == false ? Colors.black : Colors.white;
  static final audioOzge = AssetsAudioPlayer();
  static final audioDarkOzge = AssetsAudioPlayer();
  final controller = ConfettiController();
  static bool isPlaying = false;
  static bool isDarkPlaying = false;
  bool isConfettiPlaying = false;
  PermissionStatus? permissionStatus;
  bool isFileEmpty = true;
  Permission? permission;
  ImagePicker image = ImagePicker();
  XFile? img;
  // bool _selected = false;
  // Future<bool> _onWillPop() async {
  //   return (await showDialog(
  //         context: context,
  //         builder: (context) => AlertDialog(
  //           title: const Text('Are you sure?'),
  //           content: const Text('Do you want to exit?'),
  //           actions: <Widget>[
  //             TextButton(
  //               onPressed: () =>
  //                   Navigator.of(context).pop(false), //<-- SEE HERE
  //               child: const Text('No'),
  //             ),
  //             TextButton(
  //               onPressed: () =>
  //                   Navigator.of(context).pop(true), // <-- SEE HERE
  //               child: const Text('Yes'),
  //             ),
  //           ],
  //         ),
  //       )) ??
  //       false;
  // }

  @override
  void initState() {
    super.initState();
    audioOzge.open(
      Audio("assets/audios/ozge.mp3"),
      headPhoneStrategy: HeadPhoneStrategy.pauseOnUnplug,
      respectSilentMode: false,
      showNotification: false,
      autoStart: false,
    );
    audioDarkOzge.open(
      Audio("assets/audios/dramatic.mp3"),
      headPhoneStrategy: HeadPhoneStrategy.pauseOnUnplug,
      respectSilentMode: false,
      showNotification: false,
      autoStart: false,
    );
    controller.addListener(() {
      setState(() {
        isConfettiPlaying = controller.state == ConfettiControllerState.playing;
      });
    });
    audioOzge.playlistAudioFinished.listen((Playing playing) {
      setState(() {
        audioOzge.dispose();
        isPlaying = false;
      });
    });
    audioDarkOzge.playlistAudioFinished.listen((Playing playing) {
      setState(() {
        audioDarkOzge.dispose();
        isPlaying = false;
      });
    });
  }

  @override
  void dispose() {
    super.dispose();
    isPlaying = isDarkPlaying = false;
    audioOzge.dispose();
    audioDarkOzge.dispose();
  }

  showPermissionsDialog(context) => showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            backgroundColor: Colors.blueGrey.shade600,
            title: const Text("PERMISSIONS DENIED!",
                style: TextStyle(color: Colors.redAccent)),
            content: const Text(
                "You denied permission to access, please go to app settings to change permissions."),
            actions: [
              Row(
                children: [
                  const Icon(Icons.settings),
                  TextButton(
                      onPressed: () {
                        Navigator.pop(context);
                        openAppSettings();
                      },
                      child: const Text("Settings")),
                  const Spacer(),
                  const Icon(Icons.clear),
                  TextButton(
                      onPressed: () {
                        Navigator.pop(context);
                      },
                      child: const Text("Cancel"))
                ],
              ),
            ],
          );
        },
      );

  @override
  Widget build(BuildContext context) {
    // widget.widgets.addAll([
    //   const SizedBox(height: 16),
    //   Center(
    //     //IconButton to play dgko instead of name
    //     child: IconButton(
    //       onPressed: () {
    //         audioOzge.playOrPause();

    //         if (!audioOzge.isPlaying.value) {
    //           setState(() {
    //             isPlaying = false;
    //           });
    //         }

    //         setState(() {
    //           isPlaying = !isPlaying;
    //         });
    //       },
    //       icon: isPlaying == true
    //           ? const Icon(
    //               Icons.stop,
    //               color: Colors.red,
    //             )
    //           : const Icon(
    //               Icons.cake,
    //               color: Colors.pink,
    //             ), //Text(
    //       //   'Name Surname',
    //       //   style: TextStyle(
    //       //     color: Colors.purpleAccent,
    //       //     fontWeight: FontWeight.bold,
    //       //     fontSize: 16,
    //       //   ),
    //     ),
    //   ),
    //   const SizedBox(height: 16),
    //   CircleAvatar(
    //     radius: MediaQuery.of(context).size.width * 0.33,
    //     child: ClipOval(
    //       child: User.filePath == ''
    //           ? Image.file(User.file!,
    //               fit: BoxFit.fill,
    //               height: MediaQuery.of(context).size.width * 0.65,
    //               width: MediaQuery.of(context).size.width * 0.65)
    //           : Image.asset(User.filePath!,
    //               fit: BoxFit.fill,
    //               height: MediaQuery.of(context).size.width * 0.65,
    //               width: MediaQuery.of(context).size.width * 0.65),
    //     ),
    //   ),
    //   const SizedBox(height: 16),
    //   const Divider(),
    //   IconButton(
    //       color: Colors.black87,
    //       onPressed: () async {
    //         permissionStatus = await Permission.storage.request();
    //         if (permissionStatus == PermissionStatus.granted) {
    //           var t = await getTemporaryDirectory();
    //           // var p = '${t.path}/ml.jpg';
    //           final ByteData byte =
    //               await rootBundle.load('assets/light_mode/indir.jpg');
    //           final Uint8List list = byte.buffer.asUint8List();
    //           var bytes = img != null ? await img!.readAsBytes() : list;
    //           final r = await ImageGallerySaver.saveImage(
    //             bytes,
    //             name: "screenshot${generateRandomString(16)}",
    //           );
    //           String s = r['filePath'];

    //           ScaffoldMessenger.of(context).showSnackBar(
    //             SnackBar(
    //               duration: const Duration(seconds: 2),
    //               elevation: 0,
    //               behavior: SnackBarBehavior.floating,
    //               content: Text('Image downloaded to $s'),
    //             ),
    //           );
    //           print(r["filePath"]);
    //         }
    //         if (permissionStatus == PermissionStatus.denied) {
    //           ScaffoldMessenger.of(context).showSnackBar(
    //             const SnackBar(
    //               duration: Duration(seconds: 2),
    //               elevation: 0,
    //               behavior: SnackBarBehavior.floating,
    //               content: Text(
    //                   'You should give permission to change or download the profile picture.'),
    //             ),
    //           );
    //         }
    //       },
    //       icon: const Icon(Icons.download)),
    //   const Divider(),
    //   const SizedBox(height: 16),
    //   const Center(
    //     child: Text(
    //       'Greetings!',
    //       style: TextStyle(
    //         color: Colors.red,
    //         fontWeight: FontWeight.bold,
    //         fontSize: 16,
    //       ),
    //     ),
    //   ),
    //   const SizedBox(height: 16),
    //   const Divider(),
    //   TextButton(
    //     child: const Text("Click"),
    //     onPressed: () {
    //       showDialog(
    //         context: context,
    //         builder: (BuildContext context) {
    //           return AlertDialog(
    //             backgroundColor: Colors.blueAccent,
    //             title: Center(
    //               child: Image.asset("assets/gifs/hpbd.gif", fit: BoxFit.fill),
    //             ),
    //             // content:
    //             //     const Center(child: Text("Nice mutlu yıllara...")),
    //             actions: const [
    //               // TextButton(
    //               //   onPressed: () {},
    //               //   child: Image.asset("assets/spongebob.gif",
    //               //       fit: BoxFit.cover),
    //               // )
    //             ],
    //           );
    //         },
    //       );
    //     },
    //   ),
    //   const Divider(),
    //   MaterialButton(
    //     onPressed: () async {
    //       permissionStatus = await Permission.storage.request();

    //       if (permissionStatus == PermissionStatus.granted) {
    //         showDialog(
    //           context: context,
    //           builder: (BuildContext context) {
    //             return AlertDialog(
    //               title: const Text("Please choose one"),
    //               content: const Text(
    //                   "Pick an image from gallery or take one from camera."),
    //               // content:
    //               //     const Center(child: Text("Nice mutlu yıllara...")),
    //               actions: <Widget>[
    //                 Row(
    //                   children: [
    //                     const Icon(Icons.camera_alt),
    //                     TextButton(
    //                       onPressed: () async {
    //                         img = await image.pickImage(
    //                             source: ImageSource.camera);
    //                         Navigator.pop(context);
    //                         setState(() {
    //                           User.file = File(img!.path);
    //                           if (User.file != null) {
    //                             User.filePath = '';
    //                             // widget.callbackFunction();
    //                             // MyHomePageState.filePath
    //                           }
    //                         });

    //                         // final bool? isSaved =
    //                         //     await GallerySaver.saveImage(
    //                         //   p,
    //                         //   toDcim: true,
    //                         // );
    //                         // print("$isSaved!");
    //                         // ignore: use_build_context_synchronously
    //                       },
    //                       child: const Text('Camera'),
    //                     ),
    //                     const Spacer(),
    //                     const Icon(Icons.photo),
    //                     TextButton(
    //                       onPressed: () async {
    //                         img = await image.pickImage(
    //                             source: ImageSource.gallery);
    //                         Navigator.pop(context);
    //                         setState(
    //                           () {
    //                             User.file = File(img!.path);
    //                             if (User.file != null) {
    //                               User.filePath = '';
    //                               // widget.callbackFunction();
    //                               // MyHomePageState.setState(() {});
    //                             }
    //                           },
    //                         );
    //                         // ignore: use_build_context_synchronously
    //                       },
    //                       child: const Text('Gallery'),
    //                     ),
    //                   ],
    //                 ),
    //               ],
    //             );
    //           },
    //         );
    //       }
    //       if (permissionStatus == PermissionStatus.denied) {
    //         // ignore: use_build_context_synchronously
    //         widget._scaffoldKey.currentState!.showSnackBar(const SnackBar(
    //           content: Text(
    //               'You should give permission to change or download the profile picture.'),
    //           duration: Duration(seconds: 3),
    //         ));
    //       }
    //       if (permissionStatus == PermissionStatus.permanentlyDenied) {
    //         openAppSettings();
    //       }
    //     },
    //     child: const Text("Change profile picture",
    //         style: TextStyle(
    //           color: Colors.purple,
    //         )),
    //   ),
    //   const Spacer(),
    //   MaterialButton(
    //     onPressed: () {
    //       setState(() {
    //         User.filePath = "assets/light_mode/indir.jpg";
    //       });
    //     },
    //     child: const Text("Remove profile picture",
    //         style: TextStyle(color: Colors.red)),
    //   ),
    //   const Divider(),
    //   TextButton(
    //     onPressed: () {},
    //     child: const Text("Click 2.0"),
    //   ),
    // ]);
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        scaffoldBackgroundColor:
            Globals.selected == false ? Colors.greenAccent : Colors.black,
        appBarTheme: AppBarTheme(
          color: Globals.selected == false ? Colors.greenAccent : Colors.black,
        ),
        bottomAppBarTheme: BottomAppBarTheme(
          color: Globals.selected == false ? Colors.greenAccent : Colors.black,
        ),
      ),
      home: Scaffold(
          key: widget._scaffoldKey,
          bottomNavigationBar: BottomAppBar(
            child: Row(
              children: [
                const SizedBox(width: 16),
                // Container(
                //   height: 40,
                //   width: 110,
                //   alignment: Alignment.bottomLeft,
                //   child: FittedBox(
                //     child: ChoiceChip(
                //       clipBehavior: Clip.hardEdge,
                //       label: Globals.selected == true
                //           ? const Icon(Icons.dark_mode)
                //           : const Icon(Icons.light_mode),
                //       selected: Globals.selected,
                //       onSelected: (bool newValue) {
                //         if (Globals.selected == false) {
                //           showDialog<String>(
                //             barrierDismissible: true,
                //             context: context,
                //             builder: (BuildContext context) => AlertDialog(
                //               title: const Text('Activate Dark Mode',
                //                   style: TextStyle(color: Colors.redAccent)),
                //               content: const Text(
                //                   'You are about to activate the dark mode, use it carefully, you don\'t know what you are up against.\n(PS: CONFETTI DOESN\'T WORK WHEN THE DARK MODE IS ON, YOU WON\'T NEED IT ANYWAYS.)'),
                //               actions: <Widget>[
                //                 Row(
                //                   children: [
                //                     const Icon(Icons.dark_mode),
                //                     TextButton(
                //                       onPressed: () {
                //                         Navigator.pop(context, 'Cancel');
                //                         setState(() {
                //                           User.filePath =
                //                               "assets/dark_mode/default.jpg";
                //                           MyHomePageState.audioSpongeBob
                //                               .dispose();
                //                           MyHomePageState.audioDarkSpongeBob
                //                               .dispose();
                //                           audioOzge.dispose();
                //                           audioDarkOzge.dispose();
                //                           isPlaying = isDarkPlaying = false;
                //                           MyHomePageState.isPlaying =
                //                               MyHomePageState.isDarkPlaying =
                //                                   false;
                //                           Globals.selected = newValue;
                //                           colorOfDivider =
                //                               Globals.selected == false
                //                                   ? Colors.black
                //                                   : Colors.white;
                //                         });
                //                       },
                //                       child: const Text('ACTIVATE'),
                //                     ),
                //                     const Spacer(),
                //                     const Icon(Icons.light_mode),
                //                     TextButton(
                //                       onPressed: () {
                //                         Navigator.pop(context, 'Continue');
                //                       },
                //                       child: const Text('STAY'),
                //                     ),
                //                   ],
                //                 ),
                //               ],
                //             ),
                //           );
                //         } else {
                //           setState(() {
                //             User.filePath = "assets/light_mode/ozge.jpg";
                //             MyHomePageState.audioSpongeBob.dispose();
                //             MyHomePageState.audioDarkSpongeBob.dispose();
                //             audioOzge.dispose();
                //             audioDarkOzge.dispose();
                //             isPlaying = isDarkPlaying = false;
                //             Globals.selected = newValue;
                //             MyHomePageState.isPlaying =
                //                 MyHomePageState.isDarkPlaying = false;
                //             colorOfDivider = Globals.selected == false
                //                 ? Colors.black
                //                 : Colors.white;
                //           });
                //         }
                //       },
                //     ),
                //   ),
                // ),
                const Spacer(),
                Stack(
                  children: [
                    ConfettiWidget(
                      confettiController: controller,
                      shouldLoop: true,
                      blastDirectionality: BlastDirectionality.explosive,
                      emissionFrequency: 0.20,
                      numberOfParticles: 15,
                      gravity: 0.1,
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
          appBar: AppBar(
            leading: IconButton(
              onPressed: () {
                UserState.audioDarkOzge.dispose();
                UserState.isPlaying = false;
                UserState.audioOzge.dispose();
                UserState.isDarkPlaying = false;
                Navigator.pushNamed(context, '/').then((_) => setState(() {}));
                // Navigator.push(context,
                //         MaterialPageRoute(builder: (_) => MyHomePage()))
                //     .then((value) {
                //   // you have come back to the pageA, now perform your logic
                // });
              },
              color: Globals.selected == false ? Colors.black : Colors.red,
              icon: const Icon(Icons.arrow_back),
            ),
            title: FittedBox(
              child: Text(
                "Profile",
                style: TextStyle(
                  color: Globals.selected == false ? Colors.black : Colors.red,
                ),
              ),
            ),
          ),
          body: Builder(
            builder: (context) => ListView(
              clipBehavior: Clip.hardEdge,
              shrinkWrap: true,
              children: [
                const SizedBox(height: 16),
                Center(
                  //IconButton to play dgko instead of name
                  child: IconButton(
                    onPressed: () {
                      if (Globals.selected == false) {
                        audioOzge.playOrPause();

                        if (!audioOzge.isPlaying.value) {
                          setState(() {
                            isPlaying = false;
                          });
                        }

                        setState(() {
                          isPlaying = !isPlaying;
                        });
                      } else {
                        audioDarkOzge.playOrPause();
                        if (!audioDarkOzge.isPlaying.value) {
                          setState(() {
                            isPlaying = false;
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
                                Icons.stop,
                                color: Colors.red,
                              )
                            : const Icon(
                                Icons.cake,
                                color: Colors.pink,
                              ))
                        : (isDarkPlaying == true
                            ? const Icon(
                                Icons.stop,
                                color: Colors.blue,
                              )
                            : const Icon(
                                Icons.local_fire_department_sharp,
                                color: Colors.red,
                              )),
                    //Text(
                    //   'Name Surname',
                    //   style: TextStyle(
                    //     color: Colors.purpleAccent,
                    //     fontWeight: FontWeight.bold,
                    //     fontSize: 16,
                    //   ),
                  ),
                ),
                const SizedBox(height: 16),
                CircleAvatar(
                  backgroundColor: Colors.red,
                  radius: MediaQuery.of(context).size.width * 0.33,
                  child: ClipOval(
                    child: User.filePath == ''
                        ? Image.file(User.file!,
                            fit: BoxFit.fill,
                            height: MediaQuery.of(context).size.width * 0.65,
                            width: MediaQuery.of(context).size.width * 0.65)
                        : Image.asset(User.filePath!,
                            fit: BoxFit.fill,
                            height: MediaQuery.of(context).size.width * 0.65,
                            width: MediaQuery.of(context).size.width * 0.65),
                  ),
                ),
                const SizedBox(height: 16),
                Divider(color: colorOfDivider),
                IconButton(
                    color:
                        Globals.selected == false ? Colors.black87 : Colors.red,
                    onPressed: () async {
                      permissionStatus = await Permission.storage.request();
                      if (permissionStatus == PermissionStatus.granted) {
                        showDialog(
                          context: context,
                          builder: (context) => AlertDialog(
                            title: const Text("Download profile picture?"),
                            content: const Text(
                                "Current profile picture will be downloaded."),
                            actions: [
                              Row(children: [
                                const Icon(Icons.download),
                                const SizedBox(width: 8),
                                TextButton(
                                  onPressed: () async {
                                    Navigator.pop(context);
                                    var t = await getTemporaryDirectory();
                                    // var p = '${t.path}/ml.jpg';
                                    final ByteData byte = await rootBundle
                                        .load('assets/light_mode/indir.jpg');
                                    final Uint8List list =
                                        byte.buffer.asUint8List();
                                    var bytes = img != null
                                        ? await img!.readAsBytes()
                                        : list;
                                    final r = await ImageGallerySaver.saveImage(
                                      bytes,
                                      name:
                                          "screenshot${generateRandomString(16)}",
                                    );
                                    String s = r['filePath'];

                                    // ScaffoldMessenger.of(context)
                                    //     .showSnackBar(
                                    //   SnackBar(
                                    //     duration: const Duration(seconds: 2),
                                    //     elevation: 0,
                                    //     behavior: SnackBarBehavior.floating,
                                    //     content: Text('Image downloaded to $s'),
                                    //   ),
                                    // );
                                    widget._scaffoldKey.currentState!
                                        .showSnackBar(SnackBar(
                                      content: Text('Image downloaded to $s.'),
                                      duration: const Duration(seconds: 3),
                                    ));
                                    print(r["filePath"]);
                                  },
                                  child: const Text("Download"),
                                ),
                                const Spacer(),
                                const Icon(Icons.cancel),
                                TextButton(
                                  onPressed: () {
                                    Navigator.pop(context);
                                  },
                                  child: const Text("Cancel"),
                                ),
                              ]),
                            ],
                          ),
                        );
                      }
                      if (permissionStatus == PermissionStatus.denied) {
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(
                            duration: Duration(seconds: 2),
                            elevation: 0,
                            behavior: SnackBarBehavior.floating,
                            content: Text(
                                'You should give permission to change or download the profile picture.'),
                          ),
                        );
                      }
                      if (permissionStatus ==
                          PermissionStatus.permanentlyDenied) {
                        showPermissionsDialog(context);
                      }
                    },
                    icon: const Icon(Icons.download)),
                Divider(color: colorOfDivider),

                const SizedBox(height: 16),
                Padding(
                  padding: const EdgeInsets.all(16),
                  child: Globals.selected == false
                      ? const Text(
                          'Sayın Maraz Ali Bu Özge Koordi Hanım Hazretleri doğum gününüz kutlu olsun! Nice mutlu yıllara. Umarım hayallerini gerçekleştirebileceğin, dopdolu bir yıl olur. (Tam burada şarkıyı açıp konfeti patlatman gerekiyor.)',
                          style: TextStyle(
                            color: Colors.red,
                            fontWeight: FontWeight.bold,
                            fontSize: 16,
                          ),
                        )
                      : const Text(
                          '(Dark Mode Özel Yayını) Kutlama yapmanın değil geleceğini planlamanın zamanı! Bir yıl daha yaşlandın, yıllar akıp gidiyor...',
                          style: TextStyle(
                            color: Colors.red,
                            fontWeight: FontWeight.bold,
                            fontSize: 16,
                          ),
                        ),
                ),
                const SizedBox(height: 16),
                Divider(color: colorOfDivider),
                TextButton(
                  child: const Text("Click"),
                  onPressed: () {
                    showDialog(
                      context: context,
                      builder: (BuildContext context) {
                        return AlertDialog(
                          backgroundColor: Colors.blueAccent,
                          title: Center(
                            child: Globals.selected == false
                                ? Image.asset("assets/gifs/hpbd.gif",
                                    fit: BoxFit.fill)
                                : Image.asset("assets/gifs/waiting.gif",
                                    fit: BoxFit.fill),
                          ),
                          // content:
                          //     const Center(child: Text("Nice mutlu yıllara...")),
                          actions: const [
                            // TextButton(
                            //   onPressed: () {},
                            //   child: Image.asset("assets/spongebob.gif",
                            //       fit: BoxFit.cover),
                            // )
                          ],
                        );
                      },
                    );
                  },
                ),
                Divider(color: colorOfDivider),

                MaterialButton(
                  onPressed: () async {
                    permissionStatus = await Permission.storage.request();

                    if (permissionStatus == PermissionStatus.granted) {
                      showDialog(
                        context: context,
                        builder: (BuildContext context) {
                          return AlertDialog(
                            title: const Text("Please choose one"),
                            content: const Text(
                                "Pick an image from gallery or take one from camera."),
                            // content:
                            //     const Center(child: Text("Nice mutlu yıllara...")),
                            actions: <Widget>[
                              Row(
                                children: [
                                  const Icon(Icons.camera_alt),
                                  TextButton(
                                    onPressed: () async {
                                      img = await image.pickImage(
                                          source: ImageSource.camera);
                                      Navigator.pop(context);
                                      setState(() {
                                        User.file = File(img!.path);
                                        if (User.file != null) {
                                          User.filePath = '';
                                          // widget.callbackFunction();
                                          // MyHomePageState.filePath
                                        }
                                      });

                                      // final bool? isSaved =
                                      //     await GallerySaver.saveImage(
                                      //   p,
                                      //   toDcim: true,
                                      // );
                                      // print("$isSaved!");
                                      // ignore: use_build_context_synchronously
                                    },
                                    child: const Text('Camera'),
                                  ),
                                  const Spacer(),
                                  const Icon(Icons.photo),
                                  TextButton(
                                    onPressed: () async {
                                      img = await image.pickImage(
                                          source: ImageSource.gallery);
                                      Navigator.pop(context);
                                      setState(
                                        () {
                                          User.file = File(img!.path);
                                          if (User.file != null) {
                                            User.filePath = '';
                                            // widget.callbackFunction();
                                            // MyHomePageState.setState(() {});
                                          }
                                        },
                                      );
                                      // ignore: use_build_context_synchronously
                                    },
                                    child: const Text('Gallery'),
                                  ),
                                ],
                              ),
                            ],
                          );
                        },
                      );
                    }
                    if (permissionStatus == PermissionStatus.denied) {
                      // ignore: use_build_context_synchronously
                      widget._scaffoldKey.currentState!
                          .showSnackBar(const SnackBar(
                        content: Text(
                            'You should give permission to change or download the profile picture.'),
                        duration: Duration(seconds: 3),
                      ));
                    }
                    if (permissionStatus ==
                        PermissionStatus.permanentlyDenied) {
                      showPermissionsDialog(context);
                    }
                  },
                  child: const Text("Change profile picture",
                      style: TextStyle(
                        color: Colors.green,
                      )),
                ),
                //const Spacer(),
                Divider(color: colorOfDivider),

                MaterialButton(
                  onPressed: () {
                    setState(() {
                      User.filePath = Globals.selected == false
                          ? "assets/light_mode/shiro.jpg"
                          : "assets/dark_mode/metalbob.jpg";
                    });
                  },
                  child: const Text("Default profile picture",
                      style: TextStyle(color: Colors.red)),
                ),
                Divider(color: colorOfDivider),

                MaterialButton(
                    onPressed: () {
                      setState(() {
                        User.filePath = Globals.selected == false
                            ? "assets/light_mode/ozge.jpg"
                            : "assets/dark_mode/default.jpg";
                      });
                    },
                    child: Globals.selected == false
                        ? const Text("MARAZ ALİ",
                            style: TextStyle(
                                color: Color.fromARGB(255, 122, 0, 144)))
                        : const Text("ZOMBIE BOB",
                            style: TextStyle(
                                color: Color.fromARGB(255, 122, 0, 144)))),
                Divider(color: colorOfDivider),

                TextButton(
                  onPressed: () {
                    showDialog(
                      context: context,
                      builder: (BuildContext context) {
                        return AlertDialog(
                          backgroundColor: Colors.blueAccent,
                          title: Center(
                            child: Globals.selected == false
                                ? Image.asset(
                                    "assets/light_mode/silekalesi.jpg",
                                    fit: BoxFit.fill)
                                : Image.asset("assets/dark_mode/notscared.jpg",
                                    fit: BoxFit.fill),
                          ),
                        );
                      },
                    );
                  },
                  child: Globals.selected == false
                      ? const Text("Click 2.0")
                      : const Text("Safe Zone"),
                ),
              ],
            ),
          )

          // const SizedBox(height: 16),
          // Center(
          //   //IconButton to play dgko instead of name
          //   child: IconButton(
          //     onPressed: () {
          //       audioOzge.playOrPause();

          //       if (!audioOzge.isPlaying.value) {
          //         setState(() {
          //           isPlaying = false;
          //         });
          //       }

          //       setState(() {
          //         isPlaying = !isPlaying;
          //       });
          //     },
          //     icon: isPlaying == true
          //         ? const Icon(
          //             Icons.stop,
          //             color: Colors.red,
          //           )
          //         : const Icon(
          //             Icons.cake,
          //             color: Colors.pink,
          //           ), //Text(
          //     //   'Name Surname',
          //     //   style: TextStyle(
          //     //     color: Colors.purpleAccent,
          //     //     fontWeight: FontWeight.bold,
          //     //     fontSize: 16,
          //     //   ),
          //   ),
          // ),

// ListView.separated(
//   padding: const EdgeInsets.all(8),
//   itemCount: entries.length,
//   itemBuilder: (BuildContext context, int index) {
//     return Container(
//       height: 50,
//       color: Colors.amber[colorCodes[index]],
//       child: Center(child: Text('Entry ${entries[index]}')),
//     );
//   },
//   separatorBuilder: (BuildContext context, int index) => const Divider(),
// );

          //   item: [
          //     const SizedBox(height: 16),
          //     CircleAvatar(
          //       radius: MediaQuery.of(context).size.width * 0.25,
          //       child: ClipOval(
          //         child: User.filePath == ''
          //             ? Image.file(User.file!,
          //                 fit: BoxFit.fill,
          //                 height: MediaQuery.of(context).size.width * 0.65,
          //                 width: MediaQuery.of(context).size.width * 0.65)
          //             : Image.asset(User.filePath!,
          //                 fit: BoxFit.fill,
          //                 height: MediaQuery.of(context).size.width * 0.65,
          //                 width: MediaQuery.of(context).size.width * 0.65),
          //       ),
          //     ),
          //     Builder(
          //       builder: (context) => IconButton(
          //           color: Colors.black87,
          //           onPressed: () async {
          //             permissionStatus = await Permission.storage.request();
          //             if (permissionStatus == PermissionStatus.granted) {
          //               var t = await getTemporaryDirectory();
          //               // var p = '${t.path}/ml.jpg';
          //               final ByteData byte = await rootBundle
          //                   .load('assets/light_mode/indir.jpg');
          //               final Uint8List list = byte.buffer.asUint8List();
          //               var bytes =
          //                   img != null ? await img!.readAsBytes() : list;
          //               final r = await ImageGallerySaver.saveImage(
          //                 bytes,
          //                 name: "screenshot${generateRandomString(16)}",
          //               );
          //               String s = r['filePath'];

          //               ScaffoldMessenger.of(context).showSnackBar(
          //                 SnackBar(
          //                   duration: const Duration(seconds: 2),
          //                   elevation: 0,
          //                   behavior: SnackBarBehavior.floating,
          //                   content: Text('Image downloaded to $s'),
          //                 ),
          //               );
          //               print(r["filePath"]);
          //             }
          //             if (permissionStatus == PermissionStatus.denied) {
          //               ScaffoldMessenger.of(context).showSnackBar(
          //                 const SnackBar(
          //                   duration: Duration(seconds: 2),
          //                   elevation: 0,
          //                   behavior: SnackBarBehavior.floating,
          //                   content: Text(
          //                       'You should give permission to change or download the profile picture.'),
          //                 ),
          //               );
          //             }
          //           },
          //           icon: const Icon(Icons.download)),
          //     ),
          //   ],
          // ),
          // const SizedBox(height: 20),
          // const Center(
          //   child: Text(
          //     'Greetings!',
          //     style: TextStyle(
          //       color: Colors.red,
          //       fontWeight: FontWeight.bold,
          //       fontSize: 16,
          //     ),
          //   ),
          // ),
          // const Divider(),
          // TextButton(
          //   child: const Text("Click"),
          //   onPressed: () {
          //     showDialog(
          //       context: context,
          //       builder: (BuildContext context) {
          //         return AlertDialog(
          //           backgroundColor: Colors.blueAccent,
          //           title: Center(
          //             child: Image.asset("assets/gifs/hpbd.gif",
          //                 fit: BoxFit.fill),
          //           ),
          //           // content:
          //           //     const Center(child: Text("Nice mutlu yıllara...")),
          //           actions: const [
          //             // TextButton(
          //             //   onPressed: () {},
          //             //   child: Image.asset("assets/spongebob.gif",
          //             //       fit: BoxFit.cover),
          //             // )
          //           ],
          //         );
          //       },
          //     );
          //   },
          // ),
          // // const Divider(),
          // Row(
          //   children: [
          //     MaterialButton(
          //       onPressed: () async {
          //         permissionStatus = await Permission.storage.request();

          //         if (permissionStatus == PermissionStatus.granted) {
          //           showDialog(
          //             context: context,
          //             builder: (BuildContext context) {
          //               return AlertDialog(
          //                 title: const Text("Please choose one"),
          //                 content: const Text(
          //                     "Pick an image from gallery or take one from camera."),
          //                 // content:
          //                 //     const Center(child: Text("Nice mutlu yıllara...")),
          //                 actions: <Widget>[
          //                   Row(
          //                     children: [
          //                       const Icon(Icons.camera_alt),
          //                       TextButton(
          //                         onPressed: () async {
          //                           img = await image.pickImage(
          //                               source: ImageSource.camera);
          //                           setState(() {
          //                             User.file = File(img!.path);
          //                             if (User.file != null) {
          //                               User.filePath = '';
          //                               // widget.callbackFunction();
          //                               // MyHomePageState.filePath
          //                             }
          //                           });

          //                           // final bool? isSaved =
          //                           //     await GallerySaver.saveImage(
          //                           //   p,
          //                           //   toDcim: true,
          //                           // );
          //                           // print("$isSaved!");
          //                           // ignore: use_build_context_synchronously
          //                           Navigator.pop(context);
          //                         },
          //                         child: const Text('Camera'),
          //                       ),
          //                       const Spacer(),
          //                       const Icon(Icons.photo),
          //                       TextButton(
          //                         onPressed: () async {
          //                           img = await image.pickImage(
          //                               source: ImageSource.gallery);
          //                           setState(
          //                             () {
          //                               User.file = File(img!.path);
          //                               if (User.file != null) {
          //                                 User.filePath = '';
          //                                 // widget.callbackFunction();
          //                                 // MyHomePageState.setState(() {});
          //                               }
          //                             },
          //                           );
          //                           // ignore: use_build_context_synchronously
          //                           Navigator.pop(context);
          //                         },
          //                         child: const Text('Gallery'),
          //                       ),
          //                     ],
          //                   ),
          //                 ],
          //               );
          //             },
          //           );
          //         }
          //         if (permissionStatus == PermissionStatus.denied) {
          //           // ignore: use_build_context_synchronously
          //           widget._scaffoldKey.currentState!
          //               .showSnackBar(const SnackBar(
          //             content: Text(
          //                 'You should give permission to change or download the profile picture.'),
          //             duration: Duration(seconds: 3),
          //           ));
          //         }
          //         if (permissionStatus ==
          //             PermissionStatus.permanentlyDenied) {
          //           openAppSettings();
          //         }
          //       },
          //       child: const Text("Change profile picture",
          //           style: TextStyle(
          //             color: Colors.purple,
          //           )),
          //     ),
          //     const Spacer(),
          //     MaterialButton(
          //       onPressed: () {
          //         setState(() {
          //           User.filePath = "assets/light_mode/indir.jpg";
          //         });
          //       },
          //       child: const Text("Remove profile picture",
          //           style: TextStyle(color: Colors.red)),
          //     ),
          //   ],
          // ),
          // const Divider(),
          // TextButton(
          //   onPressed: () {},
          //   child: const Text("Click 2.0"),
          // ),
          // Center(
          //     child: Image.asset(
          //   "assets/indir3.png",
          //   width: 100,
          //   height: 100,
          //   fit: BoxFit.fill,
          // )),

          ),
    );
  }

  String generateRandomString(int len) {
    var r = Random();
    const _chars =
        'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890';
    return List.generate(len, (index) => _chars[r.nextInt(_chars.length)])
        .join();
  }
}
