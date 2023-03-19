<script>
    let className;
    export { className as class };
    export let name = undefined,
        id = undefined;
    export let value;
</script>

<select {name} {id} class="c {className} " bind:value>
    <slot />
</select>

<style lang="postcss" module>
    .c {
        @apply inline-flex flex-shrink-0 cursor-pointer select-none appearance-none;
        @apply h-12 pl-4 pr-10 text-sm leading-loose min-h-12;
        @apply border border-base-content border-opacity-20 bg-base-100 pr-10 font-semibold rounded-btn;
        background-image: linear-gradient(45deg, transparent 50%, currentColor 50%),
            linear-gradient(135deg, currentColor 50%, transparent 50%);
        background-position: calc(100% - 20px) calc(1px + 50%), calc(100% - 16px) calc(1px + 50%);
        background-size: 4px 4px, 4px 4px;
        background-repeat: no-repeat;
    }
    .c:focus {
        outline: 2px solid hsla(var(--bc) / 0.2);
        outline-offset: 2px;
    }
</style>
