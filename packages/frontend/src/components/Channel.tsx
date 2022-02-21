import type { Component } from "solid-js";
import type { Channel as ChannelEntity } from "../entities/Channel";

const Channel: Component<{ channel: ChannelEntity }> = ({ channel }) => {
  return (
    <div class="bg-gradient-to-tl rounded flex from-purple-700 to-blue-700 mx-3 mt-3 text-white  py-2 px-4  text-bg-dark-400 text-2xl">
      {channel.loading ? (
        <span class="animate-pulse">Loading...</span>
      ) : (
        <>
          <span class="flex-grow overflow-ellipsis overflow-hidden">
            {channel.channelId}
          </span>
          <span class="cursor-pointer flex-grow-0 flex-shrink-0 ml-3">
            Remove
          </span>
        </>
      )}
    </div>
  );
};

export default Channel;
