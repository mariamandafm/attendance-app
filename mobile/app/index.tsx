import { View, Text } from "react-native"
import { NativeWindStyleSheet } from "nativewind";
import { Link, router } from "expo-router";
import { SafeAreaView } from "react-native-safe-area-context";
import { ScrollView } from "react-native";
import CourseButton from "@/components/CourseButton";

NativeWindStyleSheet.setOutput({
    default: "native",
});

export default function App() {
    return(
        <SafeAreaView className="bg-secondary h-full">
            <ScrollView contentContainerStyle={{ height: '100%' }}>
                <View className="w-full h-full px-4">
                    <Text className="text-3xl font-pbold text-black mt-7">Your classes</Text>
                    <CourseButton 
                        title="MATH123"
                        handlePress={() => router.push("/students")}
                        containerStyles="mt-5 w-full"
                        isLoading={false}
                    />
                    <CourseButton 
                        title="MATH001"
                        handlePress={() => router.push("/students")}
                        containerStyles="mt-5 w-full"
                        isLoading={false}
                    />
                    <CourseButton 
                        title="CALC101"
                        handlePress={() => router.push("/students")}
                        containerStyles="mt-5 w-full"
                        isLoading={false}
                    />
                </View>
            </ScrollView>
        </SafeAreaView>
    );
}
