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
    const [courses, setCourses] = useState<CourseProps | null>(null);

    async function fetchCourses() {
        try {
            setLoading(true);
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
                        courses.map((course) => (
                            <CourseButton 
                                title={course.title}
                                handlePress={() => router.push("/students")}
                                containerStyles="mt-5 w-full"
                                isLoading={false}
                            />
                        
                        ))
                    }
                </View>
            </ScrollView>
        </SafeAreaView>
    );
}
