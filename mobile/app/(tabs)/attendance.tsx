import { View, Text, Button, StyleSheet } from 'react-native'
import React, {useState} from 'react'
import { CameraView, useCameraPermissions, Camera } from 'expo-camera'

const Attendance = () => {
  const [permission, requestPermission] = useCameraPermissions();
  const [image, setImage] = useState(null);

  if (!permission) {
    return (
      <View>
        <Text>Requesting permission...</Text>
      </View>
    )
  }

  if (!permission.granted) {
    return (
      <View>
        <Text>We need your permission to show the camera</Text>
        <Button onPress={requestPermission} title="grant permission" />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <CameraView
        style={styles.camera}
        facing='back'
        >
          <Text>oioioioi</Text>
      </CameraView> 
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
  },
  camera: {
    flex: 1,
  },
})

export default Attendance