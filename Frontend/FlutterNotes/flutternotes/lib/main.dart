import 'dart:async';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:geolocator/geolocator.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  CameraController? _controller;
  bool _isCameraInitialized = false;
  String _cameraError = '';
  Position? _currentPosition;

  Future<void> _initializeCamera() async {
    try {
      final cameras = await availableCameras();
      if (cameras.isEmpty) {
        throw Exception('No camera found');
      }
      _controller = CameraController(cameras.first, ResolutionPreset.high);
      await _controller!.initialize();
      setState(() {
        _isCameraInitialized = true;
      });
    } catch (e) {
      setState(() {
        _cameraError = e.toString();
      });
    }
  }

  Future<void> _requestPermissions() async {
    await [
      Permission.camera,
      Permission.locationWhenInUse,
    ].request();
  }

  Future<void> _getCurrentLocation() async {
    if (await Geolocator.isLocationServiceEnabled()) {
      bool isPermission =
          await Geolocator.checkPermission() == LocationPermission.denied
              ? (await Geolocator.requestPermission()) ==
                  LocationPermission.deniedForever
              : false;
      if (!isPermission) {
        final position = await Geolocator.getCurrentPosition();
        setState(() {
          _currentPosition = position;
        });
      }
    }
  }

  @override
  void initState() {
    super.initState();
    _initializeCamera();
    _requestPermissions();
    _getCurrentLocation();
  }

  @override
  Widget build(BuildContext context) {
    if (!_isCameraInitialized) {
      return Scaffold(
        appBar: AppBar(
          title: Text('Camera and Location Demo'),
        ),
        body: Center(
          child: CircularProgressIndicator(),
        ),
      );
    } else if (_cameraError.isNotEmpty) {
      return Scaffold(
        appBar: AppBar(
          title: Text('Camera and Location Demo'),
        ),
        body: Center(
          child: Text('Error: $_cameraError'),
        ),
      );
    } else {
      return Scaffold(
        appBar: AppBar(
          title: Text('Camera and Location Demo'),
        ),
        body: Column(
          children: <Widget>[
            Expanded(
              child: CameraPreview(_controller!),
            ),
            _currentPosition == null
                ? Text('No location data available.')
                : Text('Current Position: ${_currentPosition!}'),
          ],
        ),
      );
    }
  }
}
