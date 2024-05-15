import { View, Text, Image } from 'react-native'
import React from 'react'
import { Tabs, Redirect } from 'expo-router'

import icons  from '../../constants/icons';

interface TabIconProps {
    icon: any,
    color: string,
    name: string,
    focused: boolean
}

const TabIcon= ({icon, color, name, focused}: TabIconProps) => {
    return(
        <View className='items-center justify-center gap-1 m-1'>
            <Image
                source={icon}
                resizeMode='contain'
                tintColor={color}
                className='w-5 h-5'
            />
            <Text className={`${focused ? 'font-psemibold' : 'font-pregular'} text-xs`} style={{color:color}}>
                {name}
            </Text>
        </View>
    )
}

const TabsLayout = () => {
  return (
    <>
        <Tabs
            screenOptions={{
                tabBarShowLabel: false,
                tabBarActiveTintColor: '#002379',
                tabBarInactiveTintColor: 'gray',
                tabBarStyle: {
                    backgroundColor: 'white',
                    borderTopColor: 'transparent',
                    height: 60,
                    elevation: 0
                }
            }}
        >
            <Tabs.Screen 
                name="students" 
                options={{
                    title: 'Students',
                    headerShown: false,
                    tabBarIcon: ({color, focused}) => (
                        <TabIcon 
                            icon={icons.students} 
                            color={color} 
                            name="Students" 
                            focused={focused}/>
                    )
                }}
            />
            <Tabs.Screen 
                name="stats" 
                options={{
                    title: 'Stats',
                    headerShown: false,
                    tabBarIcon: ({color, focused}) => (
                        <TabIcon 
                            icon={icons.stats} 
                            color={color} 
                            name="Stats" 
                            focused={focused}/>
                    )
                }}
            />
            <Tabs.Screen 
                name="attendance" 
                options={{
                    title: 'Attendance',
                    headerShown: false,
                    tabBarIcon: ({color, focused}) => (
                        <TabIcon 
                            icon={icons.attendance} 
                            color={color} 
                            name="Attendance" 
                            focused={focused}/>
                    )
                }}
            />
            {/* <Tabs.Screen 
                name="attendance" 
                options={{
                    href: null
                }}
            />
            <Tabs.Screen 
                name="[class]" 
                options={{
                    href: null
                }}
            /> */}
        </Tabs>
    </>
  )
}

export default TabsLayout