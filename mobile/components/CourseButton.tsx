import { View, Text, TouchableOpacity, Image } from 'react-native'
import React from 'react'

import icons  from '../constants/icons';

interface CourseButtonProps {
  title: string,
  handlePress: () => void,
  containerStyles: string,
  isLoading: boolean

}

const CourseButton = ({title, handlePress, containerStyles, isLoading}:CourseButtonProps) => {
  return (
    <TouchableOpacity 
      onPress={handlePress}
      className={`border rounded border-2 border-primary min-h-[50px] 
                  justify-center ${containerStyles} ${isLoading} ? 'opacity-50: '`}
      disabled={isLoading}         
    >
      <Text className="px-4 text-black text-lg font-pregular ">{title}</Text>
      <Image
        source={icons.right}
        className='w-5 h-5 absolute right-4'
      />
    </TouchableOpacity>
  )
}

export default CourseButton