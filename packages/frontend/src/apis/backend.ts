import * as z from "zod";

const BASE_URL = "http://localhost:5777/api/";

class BackendError extends Error {}

const createChannelResponse = z.object({}).nullable();
export const createChannel = async (channelId: string) => {
  const response = await fetch(`${BASE_URL}channels`, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ channel_id: channelId }),
  });

  const content = await response.json();
  if (!response.ok) {
    throw new BackendError(content.detail || "Unknown error");
  }

  return createChannelResponse.parse(content);
};
