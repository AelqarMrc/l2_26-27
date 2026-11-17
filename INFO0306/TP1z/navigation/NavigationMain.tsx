import { Ionicons } from "@expo/vector-icons";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { NavigationContainer, ParamListBase, RouteProp } from "@react-navigation/native";
import MainScreen from "../screens/MainScreen";
import UserScreen from "../screens/UserScreen";

const Tab = createBottomTabNavigator();

export default function NavigationMain(){
    return(
        <NavigationContainer>
            <Tab.Navigator
                screenOptions={({route}) => ({
                    tabBarIcon: ({color, size}) => {
                        let iconName: React.ComponentProps<typeof Ionicons>['name'] = "settings";
                        if (route.name === "Accueil") 
                            iconName = "home-outline";
                        else if(route.name === "Profil")
                            iconName = "person-outline"

                        return<Ionicons name={iconName} size={size} color={color}/>
                    },
                    tabBarActiveTintColor: '#007aff',
                    tabBarInactiveTintColor: 'gray',
                    headerShown: false
                })}    
            >
                <Tab.Screen name="Accueil" component={MainScreen} />
                <Tab.Screen name="Profile" component={UserScreen} />
            </Tab.Navigator>
        </NavigationContainer>
    );
}