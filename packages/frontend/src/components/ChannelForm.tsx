import type { Component } from "solid-js";
import { createForm } from "@felte/solid";
import { useStore } from "../state";
import { createChannel } from "../apis/backend";

interface FormData {
  channelId: string;
}

const ChannelForm: Component = () => {
  const state = useStore();

  const { form } = createForm<FormData>({
    onSubmit: async (values) => {
      state.addChannel({ channelId: values.channelId, loading: true });
      try {
        const response = await createChannel(values.channelId);
        state.updateChannel({ channelId: values.channelId, loading: false });
      } catch (e) {
        console.error(e.message);
        state.setFlashMessage(e.message);
        state.removeChannel(values.channelId);
      }
    },
  });

  return (
    <form
      use:form
      class="flex mx-5 text-white mb-3 text-2xl justify-center align-middle"
    >
      <label class="py-1 pr-4" for="channelId">
        Track Channel
      </label>
      <input
        class="border rounded py-1 px-3 text-dark-400 appearance-none focus:outline-none focus:shadow-outline"
        id="channelId"
        name="channelId"
        placeholder="Channel ID"
        type="text"
      />
    </form>
  );
};

export default ChannelForm;
