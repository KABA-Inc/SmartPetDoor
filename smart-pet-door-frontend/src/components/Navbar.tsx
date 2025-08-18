import { Box, Flex, HStack, Text, Spacer, Button } from "@chakra-ui/react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <Box
      bg="brand.muted"
      px={5}
      py={2}
      shadow="md"
      position="sticky"
      top="0"
      zIndex="1000"
    >
      <Flex alignItems="center">
        <Text fontSize="md" fontWeight="bold" color="brand.solid">
          SmartPetDoor
        </Text>

        <Spacer />

        <HStack gap={3}>
          <Button
            asChild
            variant="ghost"
            color="brand.solid"
            _hover={{
              bg: "brand.muted",
              color: "brand.focusRing",
            }}
            size="sm"
          >
            <Link to="/login">Login</Link>
          </Button>
          <Button
            asChild
            color="brand.solid"
            variant="ghost"
            _hover={{
              bg: "brand.muted",
              color: "brand.focusRing",
            }}
            size="sm"
          >
            <Link to="/register">Register</Link>
          </Button>
        </HStack>
      </Flex>
    </Box>
  );
}

export default Navbar;
