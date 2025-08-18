import {
  Box,
  Button,
  Card,
  Heading,
  Input,
  Stack,
  Text,
  Link as ChackraLink,
} from "@chakra-ui/react";
import { Toaster, toaster } from "../../components/ui/toaster";
import { Link } from "react-router-dom";
import { useState } from "react";
import { login } from "../../api/auth";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {
    setLoading(true);

    try {
      await login(username, password);

      toaster.create({
        title: "Login successful",
        description: `Welcome, ${username}!`,
        type: "success",
        duration: 3000,
      });
      // navigation
    } catch (err: any) {
      toaster.create({
        title: "Login failed",
        description: err.message,
        type: "error",
        duration: 3000,
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Toaster />
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        minH="100vh"
        bg="brand.50"
        width="100vw"
      >
        <Card.Root
          w="sm"
          shadow="lg"
          borderRadius="xl"
          bg="white"
          border="1px solid"
          borderColor="brand.solid"
        >
          <Card.Header textAlign="center">
            <Heading size="lg" color="brand.solid" fontFamily="heading">
              Smart Pet Door
            </Heading>
            <Text fontSize="sm" color="gray.500">
              Please sign in to continue
            </Text>
          </Card.Header>
          <Card.Body>
            <Stack gap={4}>
              <Input
                placeholder="Username"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                borderColor="brand.muted"
                css={{ "--focus-color": "brand.solid" }}
              />
              <Input
                placeholder="Password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                borderColor="brand.muted"
                css={{ "--focus-color": "brand.solid" }}
              />
              <Button
                bg="brand.fg"
                color="white"
                _hover={{ bg: "brand.muted", borderColor: "brand.muted" }}
                onClick={handleLogin}
                loading={loading}
              >
                Login
              </Button>
              <Text textAlign="center" fontSize="sm" color="gray.600">
                Don’t have an account?{" "}
                <ChackraLink
                  asChild
                  fontWeight="bold"
                  color="brand.focusRing"
                  _hover={{ color: "brand.emphasized" }}
                >
                  <Link to="/register">Register</Link>
                </ChackraLink>
              </Text>
            </Stack>
          </Card.Body>
        </Card.Root>
      </Box>
    </>
  );
};

export default Login;
