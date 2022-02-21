import type { Component } from "solid-js";
import { useStore } from "../state";
import Channel from "./Channel";

const ChannelList: Component = () => {
  const state = useStore();

  return (
    <div class="flex flex-col">
      {state.channels.map((channel) => (
        <Channel channel={channel} />
      ))}
    </div>
  );
};

export default ChannelList;
