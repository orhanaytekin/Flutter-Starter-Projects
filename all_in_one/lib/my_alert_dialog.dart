import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'main.dart';

class MyAlertDialog extends StatelessWidget {
  final List<XFile>? _imageFileList = MyHomePage.imageFileList;
  final ImagePicker _picker = ImagePicker();
  ImagePicker image = ImagePicker();

  MyAlertDialog({super.key});

  @override
  Widget build(BuildContext context) {
    List<XFile>? imageList = MyHomePage.imageFileList;
    return FloatingActionButton(
      child: const Icon(Icons.add_photo_alternate),
      onPressed: () => showDialog<String>(
        barrierDismissible: true,
        context: context,
        builder: (BuildContext context) => AlertDialog(
          title: const Text('Add Image'),
          content: const Text(
              'Add image from gallery or take a picture from camera to make your own slide show.'),
          actions: <Widget>[
            Row(
              children: [
                const Icon(Icons.camera_alt),
                TextButton(
                  onPressed: () async {
                    XFile? img =
                        await image.pickImage(source: ImageSource.camera);
                    imageList!.add(img!);
                    int count = imageList.length;
                    // ignore: use_build_context_synchronously
                    Navigator.pop(context, 'Cancel');
                    // ignore: use_build_context_synchronously
                    ScaffoldMessenger.of(context).removeCurrentSnackBar();
                    // ignore: use_build_context_synchronously
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        duration: const Duration(seconds: 2),
                        elevation: 0,
                        behavior: SnackBarBehavior.floating,
                        content: Text("You have $count selected image(s)."),
                      ),
                    );
                  },
                  child: const Text('Camera'),
                ),
                const Spacer(),
                const Icon(Icons.photo),
                TextButton(
                  onPressed: () async {
                    int count = await selectImages();
                    // ignore: use_build_context_synchronously
                    Navigator.pop(context, 'OK');
                    // ignore: use_build_context_synchronously
                    ScaffoldMessenger.of(context).removeCurrentSnackBar();
                    // ignore: use_build_context_synchronously
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        duration: const Duration(seconds: 2),
                        elevation: 0,
                        behavior: SnackBarBehavior.floating,
                        content: Text("You have $count selected image(s)."),
                      ),
                    );

                    print("$count images total");
                  },
                  child: const Text('Gallery'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Future<int> selectImages() async {
    final List<XFile>? selectedImages = await _picker.pickMultiImage();
    if (selectedImages!.isNotEmpty) {
      _imageFileList!.addAll(selectedImages);
    }
    return _imageFileList!.length;
  }
}
