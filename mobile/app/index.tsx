import { View, Text, Alert } from "react-native"
import { NativeWindStyleSheet } from "nativewind";
import { Link, router, useFocusEffect } from "expo-router";
import { SafeAreaView } from "react-native-safe-area-context";
import { ScrollView } from "react-native";
import CourseButton from "@/components/CourseButton";

import { api } from "../lib/axios";
import { useCallback, useState } from "react";
import Loading from "@/components/Loading";

NativeWindStyleSheet.setOutput({
    default: "native",
});

type CourseProps = Array<{
    id: number;
    title: string;
    description: string;
}>

export default function App() {
    const [loading, setLoading] = useState(true);
    const [courses, setCourses] = useState<CourseProps | []>([]);

    async function fetchCourses() {
        setLoading(true);
        try {
            const response = await api.get("api/attendance/courses/");
            setCourses(response.data);
        } catch (error) {
            Alert.alert("Ops", "An error occurred while fetching courses");
        } finally {
            setLoading(false);
        }
    }

    useFocusEffect(useCallback(() => {
        fetchCourses();
    }, []))

    if (loading) {
        return <Loading />
    }

    return(
        <SafeAreaView className="bg-secondary h-full">
            <ScrollView contentContainerStyle={{ height: '100%' }}>
                <View className="w-full h-full px-4">
                    <Text className="text-3xl font-pbold text-black mt-7">Your classes</Text>
                    {
                        courses.length > 0 ? (courses.map((course) => (
                            <CourseButton 
                                key={course.id}
                                title={course.title}
                                handlePress={() => router.push("/students")}
                                containerStyles="mt-5 w-full"
                                isLoading={false}
                            />
                        
                        ))) : (
                            <Text className="text-lg text-black mt-5">No classes available</Text>
                        )
                    }
                </View>
            </ScrollView>
        </SafeAreaView>
    );
}
