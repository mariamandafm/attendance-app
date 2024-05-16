import { View, Text, ActivityIndicator } from 'react-native'
import React from 'react'

const Loading = () => {
  return (
    <View className="flex flex-1 justify-center items-center">
      <ActivityIndicator color="#002379" />
    </View>
  )
}

export default Loading