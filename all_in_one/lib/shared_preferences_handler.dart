import 'dart:convert';
import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class SharedPreferencesHandler {
  static SharedPreferences? _preferences;

  static Future init() async =>
      _preferences = await SharedPreferences.getInstance();

  static Future<bool> saveImage(List<int> imageBytes) async {
    String base64Image = base64Encode(imageBytes);
    return _preferences!.setString('image', base64Image);
  }

  static Future<Image> getImage() async {
    Uint8List bytes = base64Decode(_preferences!.getString('image')!);
    return Image.memory(bytes);
  }

  static void clear() {
    _preferences!.clear();
  }
}
